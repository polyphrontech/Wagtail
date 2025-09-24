from django.db import models
from django.db.models import Q
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index
from wagtail.documents.models import Document
from taggit.managers import TaggableManager

class ResourcePage(Page):
    description = RichTextField(blank=True)
    category = models.CharField(
        max_length=255,
        choices=[
            ('news', 'News'),
            ('guides', 'Guides'),
            ('reports', 'Reports'),
        ],
        default='news'
    )
    tags = TaggableManager(blank=True)
    file = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('category'),
        FieldPanel('tags'),
        FieldPanel('file'),
    ]
    search_fields = Page.search_fields + [
        index.SearchField('description'),
    ]

class ResourceIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    def get_context(self, request):
        context = super().get_context(request)
        resources_qs = ResourcePage.objects.child_of(self).live().order_by('-first_published_at')
        category = request.GET.get('category')
        tag = request.GET.get('tag')
        query = request.GET.get('query')
        if category:
            resources_qs = resources_qs.filter(category=category)
        if tag:
            resources_qs = resources_qs.filter(tags__name=tag)
        if query:
            resources_qs = resources_qs.filter(Q(title__icontains=query) | Q(description__icontains=query))
        from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
        paginator = Paginator(resources_qs, 10)
        page = request.GET.get('page')
        try:
            resources = paginator.page(page)
        except PageNotAnInteger:
            resources = paginator.page(1)
        except EmptyPage:
            resources = paginator.page(paginator.num_pages)
        context['resources'] = resources
        context['categories'] = ResourcePage.objects.values_list('category', flat=True).distinct()
        context['selected_category'] = category
        context['selected_tag'] = tag
        context['selected_query'] = query
        return context