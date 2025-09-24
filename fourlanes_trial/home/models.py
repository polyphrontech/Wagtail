from django.db import models
from wagtail.models import Page
from wagtail.fields import StreamField, RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import CharBlock, TextBlock, StructBlock, RichTextBlock, URLBlock, ChoiceBlock
from wagtail.images.blocks import ImageChooserBlock

class ImageCaptionBlock(StructBlock):
    image = ImageChooserBlock()
    caption = CharBlock(required=False)
    class Meta:
        template = 'home/blocks/image_caption.html'
        icon = 'image'

class QuoteBlock(StructBlock):
    quote = TextBlock()
    attribution = CharBlock(required=False)
    class Meta:
        template = 'home/blocks/quote.html'
        icon = 'openquote'

class StatisticBlock(StructBlock):
    number = CharBlock()
    label = CharBlock()
    class Meta:
        template = 'home/blocks/statistic.html'
        icon = 'tick'

class CTABlock(StructBlock):
    title = CharBlock()
    text = TextBlock()
    button_link = URLBlock()
    background_color = ChoiceBlock(choices=[
        ('bg-blue-500', 'Blue'),
        ('bg-green-500', 'Green'),
    ], required=False)
    class Meta:
        template = 'home/blocks/cta.html'
        icon = 'link'

class HomePage(Page):
    body = StreamField([
        ('rich_text', RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'bold', 'italic', 'underline', 'ol', 'ul', 'link'])),
        ('image_caption', ImageCaptionBlock()),
        ('quote', QuoteBlock()),
        ('statistic', StatisticBlock()),
        ('cta', CTABlock()),
    ], use_json_field=True, null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]