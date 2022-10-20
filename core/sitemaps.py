from django.contrib.sitemaps import Sitemap
from .models import event
from django.urls import reverse




# class PostSitemap(Sitemap):
# 	changefreq = 'weekly'
# 	priority = 0.9
# 	def items(self):
# 		return event.objects.all()
# 	def lastmod(self, obj):
# 		return obj.updated


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return [
				'denied',
				'about',
				'gallery',
				'news',
				'courses',
				'apply',
				'timetable',
				'calendar',
]

    def location(self, item):
        return reverse(item)






