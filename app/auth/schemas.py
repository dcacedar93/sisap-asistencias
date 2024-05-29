
class ModuleSchema:
    """
        * Genera un esquema en base a las clases Module y View
        * @function dump: transforma el objeto a un diccionario con la siguiente estructura
            {
                'id': string,
                'name': string,
                'views': [
                    {
                        'id': string,
                        'name': string
                    }
                ]
            }
    """
    def __init__(self, module, views=None):
        self.module = module

        if not views:
            self.views = []
        else:
            self.views = views

    def dump(self):
        serialize = {
            'id': self.module.get('id'),
            'name': self.module.get('name'),
            'views': []
        }
        views = list(map(lambda view: {'id': view.idvista, 'name': view.nombre}, self.views))
        serialize['views'] = views
        return serialize
