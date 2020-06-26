# +----------------------+
# | Internationalization |
# +----------------------+
# makemessages -l en -l zh_Hant -l zh_Hans -l de -l es -l fr -l ja -l ko -l ru -l th -l vi
# makemessages -a
# compilemessages
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
    os.path.join(BASE_DIR, 'apps', '_v_hitcount', 'locale'),
    os.path.join(BASE_DIR, 'apps', '_x_admin_honeypot', 'locale'),
    os.path.join(BASE_DIR, 'apps', '_y_axes', 'locale'),
]
LANGUAGE_CODE = 'zh-Hant'
LANGUAGES = (
    ('en', _('English')),
    ('zh-hans', _('Chinese (Simplified)')),
    ('zh-hant', _('Chinese (Traditional)')),
    ('de', _('German')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('ja', _('Japanese')),
    ('ko', _('Korean')),
    ('ru', _('Russian')),
    ('th', _('Thai')),
    ('vi', _('Vietnamese')),
)
TIME_ZONE = 'Asia/Taipei'
USE_I18N = True
USE_L10N = True
USE_TZ = True
USE_THOUSAND_SEPARATOR = True