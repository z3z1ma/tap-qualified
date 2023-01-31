<h1 align="center">Tap-Qualified</h1>

<p align="center">
<a href="https://github.com/z3z1ma/tap-qualified/blob/main/LICENSE"><img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

`tap-qualified` is a Singer tap for [Qualified](https://www.qualified.com/).

Qualified helps companies generate pipeline, faster. Tap into your greatest asset - your website - to identify your most valuable visitors, instantly start sales conversations, schedule  meetings, convert outbound and paid traffic, and uncover signals of buying intent.

Install from [PyPi](https://pypi.org/project/tap-qualified/):

```bash
pipx install tap-qualified
```

## Configuration

### Accepted Config Options

| Setting             | Required | Default | Description |
|:--------------------|:--------:|:-------:|:------------|
| api_key             | True     | None    | The token to authenticate against the API service |
| user_agent          | False    | Harness.io/Tap Qualified | The user agent to use when making requests to the API service |
| stream_maps         | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html). |
| stream_map_config   | False    | None    | User-defined config values to be used within map expressions. |
| flattening_enabled  | False    | None    | 'True' to enable schema flattening and automatically expand nested properties. |
| flattening_max_depth| False    | None    | The max depth to flatten schemas. |

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-qualified --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

Reach out to your account executive to inquire about API access.

## Usage

You can easily run `tap-qualified` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-qualified --version
tap-qualified --help
tap-qualified --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_qualified/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-qualified` CLI interface directly using `poetry run`:

```bash
poetry run tap-qualified --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._


Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-qualified
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-qualified --version
# OR run a test `elt` pipeline:
meltano elt tap-qualified target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.
