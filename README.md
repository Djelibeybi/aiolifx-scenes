# aiolifx-scenes

An async library with a single input and a single output.

If you feed it a LIFX Cloud API Personal Access Token (PAT), it will return all the scenes you that token has access to on the LIFX Cloud.


## Usage

To generate a personal access token:

1. visit <https://cloud.lifx.com> and login using the same login credentials that you use for the LIFX smart phone app.
2. Once logged in, click the arrow next to your email in the top right-hand corner of the "Cloud home" page to reveal the menu.
3. With the menu revealed, click the "Personal access tokens" menu item.
4. On the personal access tokens page, click the big blue "Generate new token" button.

Once you have a personal access token, you can install the library:

```bash
$ pip install aiolifx-scenes
```

With the library installed, you can call it from your application:

```python
import aiolifx_scenes

PAT = "personal access token"

scenes = await aiolifx_scenes.async_get_scenes(token=PAT)
```

*Top tip:* use `aiolifx_scenes.get_scenes()` from non-async methods.

## Sanity checks

An extremely basic command-line tool is provided to enable easier sanity checking of your personal access token and existing LIFX scene information.

To use the tool, set the `LIFX_API_TOKEN` environment variable, then run  `lifx-scenes`. If human readability is important to you, consider piping the output through `jq`.

For example:

```bash
$ LIFX_API_TOKEN="your_lifx_api_personal_access_token" lifx-scenes | jq
[
    {
        'uuid': '031f1116-034f-4d92-a1f3-13420e532706',
        'name': 'My Scene',
        'account': {'uuid': 'bda95b31-948c-4c34-a330-c5f0c5eeb2a3'},
        'states': [
            {
                "selector": "id:d073d5xxxxxx",
                "power": "off",
                "brightness": 0.25,
                "color": {
                "hue": 0,
                "saturation": 0,
                "kelvin": 3500
                }
            },
            {
                "selector": "id:d073d5xxxxxx",
                "power": "off",
                "brightness": 0.25,
                "color": {
                "hue": 0,
                "saturation": 0,
                "kelvin": 2500
                }
            }
        ],
        'created_at': 1658591387,
        'updated_at': 1679022191
    }
]
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
