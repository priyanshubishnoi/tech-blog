from pelican import signals

def add_ga4_to_context(generator, metadata):
    ga4 = generator.settings.get('GA4_MEASUREMENT_ID')
    if ga4:
        generator.context['GA4_MEASUREMENT_ID'] = ga4

def register():
    signals.page_generator_context.connect(add_ga4_to_context)
    signals.article_generator_context.connect(add_ga4_to_context)