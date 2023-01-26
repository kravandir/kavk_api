from setuptools import find_packages, setup

setup(
        name = 'avk_api',
        version='0.0.2',
        url='https://github.com/kravandir/avk_api/',
        download_url='https://github.com/kravandir/avk_api/archive/v{}.zip'.format('0.0.2'),
        package_dir={'': 'avk_api'},
        packages=find_packages('', include='avk_api'),
        description='Asynchronus and easy VK API',
        requires=['aiohttp', 'asyncio_atexit'],
        license='MIT License'
        )
