# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## Unreleased
[source](https://github.com/miniscruff/python-command-center/tree/master)
[compare](https://github.com/miniscruff/python-command-center/compare/v0.0.4...master)
### Removed
- Completed output at the end of running the command

## 0.0.5 - 2018-05-28
[source](https://github.com/miniscruff/python-command-center/tree/v0.0.5)
[compare](https://github.com/miniscruff/python-command-center/compare/v0.0.4...v0.0.5)

## Fixed
- click missing from install requirements
- utils and pccgui missing from package

## 0.0.4 - 2018-05-28
[source](https://github.com/miniscruff/python-command-center/tree/v0.0.4)
[compare](https://github.com/miniscruff/python-command-center/compare/v0.0.2...v0.0.4)

### Added
- Changelog
- pcc command will now run commands from keys
- pcc --commands will display the list of available commands

### Changed
- pcc-gui will now open the gui window

### Removed
- Support for package.json scripts, didnt quite work as expected
- Support for extra commands in gui mode, may add back later

## 0.0.3 - Skipped due to failed pypi upload

## 0.0.2 - 2018-05-28
[source](https://github.com/miniscruff/python-command-center/tree/v0.0.2)
[compare](https://github.com/miniscruff/python-command-center/compare/v0.0.1...v0.0.2)

### Added
- Getting started documentation in the readme

## 0.0.1 - 2018-04-22
[source](https://github.com/miniscruff/python-command-center/tree/v0.0.1)

### Added
- Default gui window from pcc.json
- Attempted support for package.json and npm
- Column arg to customize the number of columns
- Extra args can be added by key value pairs to the gui
