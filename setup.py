from setuptools import setup
setup(name='pdf_quench',
        version='1.0.5',
        description='A visual tool for cropping pdf files.',
        data_files=[('/usr/share/applications/', ['debian/usr/share/applications/pdf-quench.desktop']),
            ('usr/share/icons/hicolor/scalable/apps', ['debian/usr/share/icons/pdf-quench.svg'])],
        packages=['pdf_quench'],
        entry_points={
            'console_scripts': [
                'pdf-quench=pdf_quench:main',
            ],
        },
)

