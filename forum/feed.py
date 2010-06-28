try:
    from django.contrib.syndication.views import Feed, FeedDoesNotExist
    old_version = False
except:
    from django.contrib.syndication.feeds import Feed, FeedDoesNotExist
    old_version = True

from django.http import HttpResponse
from django.utils.translation import ugettext as _
from models import Question
from forum import settings


class RssQuestionFeed(Feed):
    copyright = settings.APP_COPYRIGHT

    def __init__(self, question_list, title, description, request):
        self._title = title
        self._description = description
        self._question_list = question_list
        self._url = request.path + "&" + "&".join(["%s=%s" % (k, v) for k, v in request.GET.items() if not k in ('page', 'pagesize', 'sort')])

        if old_version:
            super(RssQuestionFeed, self).__init__('', request)

    def title(self):
        return self._title

    def link(self):
        return self._url

    def item_link(self, item):
        return item.get_absolute_url()

    def item_author_name(self, item):
        return item.author.username

    def item_author_link(self, item):
        return item.author.get_profile_url()

    def item_pubdate(self, item):
        return item.added_at

    def item_categories(self, item):
        return item.tagname_list()  

    def items(self, item):
       return self._question_list[:30]

    if old_version:
        def __call__(self, request):
            feedgen = self.get_feed('')
            response = HttpResponse(mimetype=feedgen.mime_type)
            feedgen.write(response, 'utf-8')
            return response
            
