# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'SAC Cyberpatriots Ver: 5.0.1'
copyright = '2023, Santa Ana College & CyberPatriot Authors/Contributors - Ver. 4.1.7'
author = 'Nathaniel Clay'

release = '5.0'
version = '5.0.1'

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

html_theme_path = ["_themes"]
html_theme = "sphinx_rtd_theme"
html_logo = '_static/cyberlogo.png'
html_theme_options = {
    "logo_only": True,
    "display_version": False
}

# -- Options for EPUB output
epub_show_urls = 'footnote'


