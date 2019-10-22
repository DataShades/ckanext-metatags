import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class MetatagsPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'metatags_social_share_image': metatags_social_share_image
        }


def metatags_social_share_image():
    return toolkit.config.get('metatags.social_share.image')
