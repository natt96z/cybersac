# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Santa Ana College Cyberpatriot's Ver: 3.2.0'
copyright = '2023, Santa Ana College & CyberPatriot Authors/Contributors'
author = 'Nathaniel Clay'

release = '3.0'
version = '3.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = '_img/logo.png'
html_theme_options = {
    "logo_only": False,
    "display_version": True
}


# -- Options for EPUB output
epub_show_urls = 'footnote'

