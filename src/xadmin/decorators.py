


def register(*models, **kwargs):
    """
    Registers the given model(s) classes and wrapped ModelAdmin class with
    admin site:

    @register(Author)
    class AuthorAdmin(admin.ZKModelAdmin):
        pass

    A kwarg of `site` can be passed as the admin site, otherwise the default
    admin site will be used.
    """
    from src.xadmin.kernel import ZModelAdmin
    from src.xadmin.sites import z_site, ZAdminSite

    def _model_admin_wrapper(admin_class):
        if not models:
            raise ValueError('At least one model must be passed to register.')
        admin_site = kwargs.pop('site', z_site)
        if not isinstance(admin_site, ZAdminSite):
            raise ValueError('site must subclass ZKAdminSite')
        if not issubclass(admin_class, ZModelAdmin):
            raise ValueError('Wrapped class must subclass ZKModelAdmin.')
        admin_site.register(models, admin_class=admin_class)
        return admin_class

    return _model_admin_wrapper