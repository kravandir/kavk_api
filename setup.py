from setuptools import find_packages, setup

version = '0.1'
url = 'https://github.com/kravandir/avk_api/'

setup(
        name = 'avk_api',
        version=version,
        url=url,
        download_url=url+'archive/v{}.zip'.format(version),
        # package_dir={'': 'avk_api'},
        # packages=find_packages('', include='avk_api'),
        description='Asynchronus and easy VK API',
        requires=['aiohttp', 'asyncio_atexit'],
        license='MIT License'
        )
