#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Kedro documentation build configuration file, created by
# sphinx-quickstart on Mon Dec 18 11:31:24 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import importlib
import os
import re
import shutil
import sys
from distutils.dir_util import copy_tree
from inspect import getmembers, isclass, isfunction
from pathlib import Path
from typing import List, Tuple

from click import secho, style
from recommonmark.transform import AutoStructify

from kedro import __version__ as release

# -- Project information -----------------------------------------------------

project = "Kedro"
copyright = "2021, QuantumBlack Visual Analytics Limited"
author = "QuantumBlack"

# The short X.Y version.
version = re.match(r"^([0-9]+\.[0-9]+).*", release).group(1)


# -- General configuration ---------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "nbsphinx",
    "recommonmark",
    "sphinx_copybutton",
]

# enable autosummary plugin (table of contents for modules/classes/class
# methods)
autosummary_generate = True
autosummary_generate_overwrite = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "**.ipynb_checkpoints",
    "_templates",
    "modules.rst",
    "source",
    "README.md"
]

type_targets = {
    "py:class": (
        "object",
        "bool",
        "int",
        "float",
        "str",
        "tuple",
        "Any",
        "Dict",
        "typing.Dict",
        "typing.Iterable",
        "typing.List",
        "typing.Tuple",
        "typing.Type",
        "typing.Set",
        "kedro.config.config.ConfigLoader",
        "kedro.io.core.AbstractDataSet",
        "kedro.io.core.AbstractVersionedDataSet",
        "kedro.io.core.DataSetError",
        "kedro.io.core.Version",
        "kedro.io.data_catalog.DataCatalog",
        "kedro.io.transformers.AbstractTransformer",
        "kedro.io.data_catalog_with_default.DataCatalogWithDefault",
        "kedro.io.partitioned_data_set.PartitionedDataSet",
        "kedro.pipeline.pipeline.Pipeline",
        "kedro.runner.runner.AbstractRunner",
        "kedro.runner.parallel_runner._SharedMemoryDataSet",
        "kedro.versioning.journal.Journal",
        "kedro.framework.context.context.KedroContext",
        "kedro.framework.startup.ProjectMetadata",
        "kedro.framework.project.settings.ProjectSettings",
        "abc.ABC",
        "pathlib.Path",
        "pathlib.PurePosixPath",
        "requests.auth.AuthBase",
        "google.oauth2.credentials.Credentials",
        "Exception",
        "CONF_ROOT",
        "integer -- return number of occurrences of value",
        "integer -- return first index of value.",
    ),
    "py:data": (
        "typing.Any",
        "typing.Callable",
        "typing.Union",
        "typing.Optional",
        "typing.Tuple",
    ),
    "py:exc": (
        "ValueError",
        "MissingConfigException",
        "DataSetError",
        "ImportError",
        "KedroCliError",
        "Exception",
        "TypeError",
        "SyntaxError",
        "CircularDependencyError",
        "OutputNotUniqueError",
        "ConfirmNotUniqueError",
    ),
}

# https://stackoverflow.com/questions/61770698/sphinx-nit-picky-mode-but-only-for-links-i-explicitly-wrote
nitpick_ignore = [(key, value) for key in type_targets for value in type_targets[key]]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
here = Path(__file__).parent.absolute()
html_logo = str(here / "kedro_logo.svg")

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"collapse_navigation": False, "style_external_links": True}

# some of these complain that the sections don't exist (which is not true),
# too many requests, or forbidden URL
linkcheck_ignore = [
    "https://www.datacamp.com/community/tutorials/docstrings-python",  # "forbidden" url
    "https://setuptools.readthedocs.io/en/latest/setuptools.html#dynamic-discovery-of-services-and-plugins",
    "https://github.com/argoproj/argo/blob/master/README.md#quickstart",
    "https://console.aws.amazon.com/batch/home#/jobs",
    "https://github.com/EbookFoundation/free-programming-books/blob/master/books/free-programming-books.md#python",
    "https://github.com/jazzband/pip-tools#example-usage-for-pip-compile",
    "https://www.astronomer.io/docs/cloud/stable/get-started/quickstart#",
    "https://github.com/quantumblacklabs/private-kedro/blob/master/kedro/templates/project/*",
    "https://zenodo.org/record/4336685",
    "https://zenodo.org/badge/latestdoi/182067506",
]

# retry before render a link broken (fix for "too many requests")
linkcheck_retries = 5
linkcheck_rate_limit_timeout = 2.0

html_context = {
    "display_github": True,
    "github_url": "https://github.com/quantumblacklabs/kedro/tree/master/docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_show_sourcelink = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Kedrodoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "Kedro.tex", "Kedro Documentation", "QuantumBlack", "manual")
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "kedro", "Kedro Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Kedro",
        "Kedro Documentation",
        author,
        "Kedro",
        "Kedro is a Data Science framework for QuantumBlack-led projects.",
        "Data-Science",
    )
]

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Extension configuration -------------------------------------------------

# nbsphinx_prolog = """
# see here for prolog/epilog details:
# https://nbsphinx.readthedocs.io/en/0.3.1/prolog-and-epilog.html
# """

nbsphinx_epilog = """
.. note::

     Found a bug, or didn't find what you were looking for? 🙏 `Please file a
     ticket <https://github.com/quantumblacklabs/kedro/issues/new/choose>`_
"""

# -- NBconvert kedro config -------------------------------------------------
nbsphinx_kedro_name = "kedro"

# -- Kedro specific configuration -----------------------------------------
KEDRO_MODULES = [
    "kedro.io",
    "kedro.pipeline",
    "kedro.runner",
    "kedro.config",
    "kedro.extras.datasets",
    "kedro.extras.logging",
    "kedro.extras.decorators",
    "kedro.extras.transformers",
]


def get_classes(module):
    importlib.import_module(module)
    return [obj[0] for obj in getmembers(sys.modules[module], lambda obj: isclass(obj))]


def get_functions(module):
    importlib.import_module(module)
    return [
        obj[0] for obj in getmembers(sys.modules[module], lambda obj: isfunction(obj))
    ]


def remove_arrows_in_examples(lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace(">>>", "")


def autolink_replacements(what: str) -> List[Tuple[str, str, str]]:
    """
    Create a list containing replacement tuples of the form:
    (``regex``, ``replacement``, ``obj``) for all classes and methods which are
    imported in ``KEDRO_MODULES`` ``__init__.py`` files. The ``replacement``
    is a reStructuredText link to their documentation.

    For example, if the docstring reads:
        This LambdaDataSet loads and saves ...

    Then the word ``LambdaDataSet``, will be replaced by
    :class:`~kedro.io.LambdaDataSet`

    Works for plural as well, e.g:
        These ``LambdaDataSet``s load and save

    Will convert to:
        These :class:`kedro.io.LambdaDataSet` load and save

    Args:
        what: The objects to create replacement tuples for. Possible values
            ["class", "func"].

    Returns:
        A list of tuples: (regex, replacement, obj), for all "what" objects
        imported in __init__.py files of ``KEDRO_MODULES``.

    """
    replacements = []
    suggestions = []
    for module in KEDRO_MODULES:
        if what == "class":
            objects = get_classes(module)
        elif what == "func":
            objects = get_functions(module)

        # Look for recognised class names/function names which are
        # surrounded by double back-ticks
        if what == "class":
            # first do plural only for classes
            replacements += [
                (r"``{}``s".format(obj), f":{what}:`~{module}.{obj}`\\\\s", obj,)
                for obj in objects
            ]

        # singular
        replacements += [
            (r"``{}``".format(obj), f":{what}:`~{module}.{obj}`", obj)
            for obj in objects
        ]

        # Look for recognised class names/function names which are NOT
        # surrounded by double back-ticks, so that we can log these in the
        # terminal
        if what == "class":
            # first do plural only for classes
            suggestions += [
                (r"(?<!\w|`){}s(?!\w|`{{2}})".format(obj), f"``{obj}``s", obj)
                for obj in objects
            ]

        # then singular
        suggestions += [
            (r"(?<!\w|`){}(?!\w|`{{2}})".format(obj), f"``{obj}``", obj)
            for obj in objects
        ]

    return replacements, suggestions


def log_suggestions(lines: List[str], name: str):
    """Use the ``suggestions`` list to log in the terminal places where the
    developer has forgotten to surround with double back-ticks class
    name/function name references.

    Args:
        lines: The docstring lines.
        name: The name of the object whose docstring is contained in lines.
    """
    title_printed = False

    for i in range(len(lines)):
        if ">>>" in lines[i]:
            continue

        for existing, replacement, obj in suggestions:
            new = re.sub(existing, r"{}".format(replacement), lines[i])
            if new == lines[i]:
                continue
            if ":rtype:" in lines[i] or ":type " in lines[i]:
                continue

            if not title_printed:
                secho("-" * 50 + "\n" + name + ":\n" + "-" * 50, fg="blue")
                title_printed = True

            print(
                "["
                + str(i)
                + "] "
                + re.sub(existing, r"{}".format(style(obj, fg="magenta")), lines[i])
            )
            print(
                "["
                + str(i)
                + "] "
                + re.sub(existing, r"``{}``".format(style(obj, fg="green")), lines[i])
            )

    if title_printed:
        print("\n")


def autolink_classes_and_methods(lines):
    for i in range(len(lines)):
        if ">>>" in lines[i]:
            continue

        for existing, replacement, obj in replacements:
            lines[i] = re.sub(existing, r"{}".format(replacement), lines[i])


def autodoc_process_docstring(app, what, name, obj, options, lines):
    try:
        # guarded method to make sure build never fails
        log_suggestions(lines, name)
        autolink_classes_and_methods(lines)
    except Exception as e:
        print(
            style(
                "Failed to check for class name mentions that can be "
                "converted to reStructuredText links in docstring of {}. "
                "Error is: \n{}".format(name, str(e)),
                fg="red",
            )
        )

    remove_arrows_in_examples(lines)


def skip(app, what, name, obj, skip, options):
    if name == "__init__":
        return False
    return skip


def _prepare_build_dir(app, config):
    """Get current working directory to the state expected
    by the ReadTheDocs builder. Shortly, it does the same as
    ./build-docs.sh script except not running `sphinx-build` step."""
    build_root = Path(app.srcdir)
    build_out = Path(app.outdir)
    copy_tree(str(here / "source"), str(build_root))
    copy_tree(str(build_root / "14_api_docs"), str(build_root))
    shutil.rmtree(str(build_root / "14_api_docs"))
    shutil.rmtree(str(build_out), ignore_errors=True)
    copy_tree(str(build_root / "css"), str(build_out / "_static" / "css"))
    shutil.rmtree(str(build_root / "css"))


def env_override(default_appid):
    build_version = os.getenv("READTHEDOCS_VERSION")

    if build_version == "latest":
        return os.environ["HEAP_APPID_QA"]
    if build_version == "stable":
        return os.environ["HEAP_APPID_PROD"]

    return default_appid  # default to Development for local builds


def _add_jinja_filters(app):
    # https://github.com/crate/crate/issues/10833
    from sphinx.builders.latex import LaTeXBuilder
    from sphinx.builders.linkcheck import CheckExternalLinksBuilder

    # LaTeXBuilder is used in the PDF docs build,
    # and it doesn't have attribute 'templates'
    if not (
        isinstance(app.builder, LaTeXBuilder)
        or isinstance(app.builder, CheckExternalLinksBuilder)
    ):
        app.builder.templates.environment.filters["env_override"] = env_override


def setup(app):
    app.connect("config-inited", _prepare_build_dir)
    app.connect("builder-inited", _add_jinja_filters)
    app.connect("autodoc-process-docstring", autodoc_process_docstring)
    app.connect("autodoc-skip-member", skip)
    app.add_css_file("css/qb1-sphinx-rtd.css")
    # fix a bug with table wraps in Read the Docs Sphinx theme:
    # https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
    app.add_css_file("css/theme-overrides.css")
    # enable rendering RST tables in Markdown
    app.add_config_value("recommonmark_config", {"enable_eval_rst": True}, True)
    app.add_transform(AutoStructify)


def fix_module_paths():
    """
    This method fixes the module paths of all class/functions we import in the
    __init__.py file of the various kedro submodules.
    """
    for kedro_module in KEDRO_MODULES:
        mod = importlib.import_module(kedro_module)
        mod.__all__ = get_classes(kedro_module) + get_functions(kedro_module)


# (regex, restructuredText link replacement, object) list
replacements = []

# (regex, class/function name surrounded with back-ticks, object) list
suggestions = []

try:
    # guarded code to make sure build never fails
    replacements_f, suggestions_f = autolink_replacements("func")
    replacements_c, suggestions_c = autolink_replacements("class")
    replacements = replacements_f + replacements_c
    suggestions = suggestions_f + suggestions_c
except Exception as e:
    print(
        style(
            "Failed to create list of (regex, reStructuredText link "
            "replacement) for class names and method names in docstrings. "
            "Error is: \n{}".format(str(e)),
            fg="red",
        )
    )

fix_module_paths()
