# django compressor and less-c compiler

COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (('text/less', 'lessc {infile} {outfile}'),)

# django mobileesp

from django_mobileesp.detector import agent

DETECT_USER_AGENTS = {
    'is_tablet' : agent.detectTierTablet,
    'is_mobile': agent.detectMobileQuick,
}

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)
