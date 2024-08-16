# LSTE Plugin: Excerpts Markdown

This plugin for [Lauras Simple Template Engine (LSTE)](https://github.com/lauratheq/lste) processes excerpts by converting them from Markdown to HTML. It allows you to write your excerpts in Markdown format, making it easier to format text, include code blocks, tables, and more within your site content.

## Usage

### Installation

1. Add the plugin to your LSTE configuration by including it in your `.listerc` file:

    ```ini
    [plugins]
    excerpts-markdown = lauratheq/excerpts-markdown.lste
    ```

2. LSTE will automatically download and activate the plugin during the next site generation.

### Configuration

There is no further configuration needed.

## Contributing

### Contributor Code of Conduct

Please note that this project is adapting the [Contributor Code of Conduct](https://learn.wordpress.org/online-workshops/code-of-conduct/) from WordPress.org even though this is not a WordPress project. By participating in this project, you agree to abide by its terms.

### Basic Workflow

* Grab an issue
* Fork the project
* Add a branch with the number of your issue
* Develop your changes
* Commit to your forked project
* Send a pull request to the main branch with all the details

Please make sure that you have [set up your user name and email address](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) for use with Git. Strings such as `silly nick name <root@localhost>` look unprofessional in the commit history of a project.

Due to time constraints, you may not always get a quick response. Please do not take delays personally and feel free to send a reminder.

### Workflow Process

* Every new issue gets the label 'Request'
* Every commit must be linked to the issue with the following pattern: `#${ISSUENUMBER} - ${MESSAGE}`
* Every PR should contain one commit and reference a specific issue
