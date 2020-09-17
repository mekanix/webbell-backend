from freenit.api import register_endpoints


def create_api(app):
    from .medic import blueprint as medic
    register_endpoints(
        app,
        '/api/v0',
        [medic],
    )
