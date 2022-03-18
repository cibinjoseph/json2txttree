from setuptools import setup
import c81utils


setup(name='json2txttree',
      version=c81utils.__version__,
      author='Cibin Joseph',
      author_email='cibinjoseph92@gmail.com',
      url='http://pypi.python.org/pypi/json2txttree',
      description='Library for pretty printing json data to txt files',
      long_description='\n'.join([
          open('README.rst', 'r').read(),
          open('CHANGES.rst', 'r').read()]),
      long_description_content_type='text/x-rst',
      keywords='json',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Science/Research',
          'Operating System :: OS Independent',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Database'],
      python_requires='>=3',
      license='MIT',
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      py_modules=['json2txttree'],
      test_suite='test_json2txttree.main',
     )
