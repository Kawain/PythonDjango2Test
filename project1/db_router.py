class DbRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'notes'
        elif model._meta.app_label == 'app2':
            return 'notes'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'notes'
        elif model._meta.app_label == 'app2':
            return 'notes'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'app1' or obj2._meta.app_label == 'app1':
            return True
        elif obj1._meta.app_label == 'app2' or obj2._meta.app_label == 'app2':
            return True

    def allow_migrate(self, db, app_label, model=None, **hints):
        if app_label == 'app1':
            return db == 'notes'
        elif app_label == 'app2':
            return db == 'notes'
