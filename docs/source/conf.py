# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Assistant'
copyright = '2024, YOLO'
author = 'YOLO'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',        # Automatically include docstrings
    'sphinx.ext.napoleon',       # Support for Google style docstrings
    'sphinx.ext.viewcode',       # Add links to highlighted source code
    'sphinx.ext.githubpages',    # Publish on GitHub Pages (optional)
]


templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
import sphinx_rtd_theme

html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
