# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Documentation Hub Ver: 2.2.4'
copyright = '2022, Santa Ana College & CyberPatriot Authors/Contributors'
author = 'Nathaniel Clay'

release = '2.4'
version = '2.2.4'

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

# -- Options for EPUB output
epub_show_urls = 'footnote'
