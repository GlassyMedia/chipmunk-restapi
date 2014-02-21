# chipmunk-restapi

A REST API backend server for the [Chipmunk Chrome extension](https://github.com/GlassyMedia/chipmunk-chrome-extension)

## Usage

### Dependencies

```sh
pip install -r requirements.txt
```

### Configuration

This program needs to acces your Google Drive. We are hardcoding a Google login as environment variables for now.
You need to set `GOOGLE_USER` and `GOOGLE_PASS` for both regular use and unit testing.

```
export GOOGLE_USER=<USERNAME>
export GOOGLE_PASS=<PASSWORD>
```

Where `<USERNAME>` and `<PASSWORD>` are your Google login information.

Alternatively, you can make use of the `.env` file in the root folder if you are running with Heroku Foreman.

### Run

```
gunicorn server:app
```

Or with Heroku Foreman,

```
foreman start
```

### Testing

Install nose.

```sh
pip install nose
```

In addition to the Google login environment variables, you'll also need to set
`TEST_WORKSHEET_KEY` to specify your test worksheet in your account. You can
get your worksheet key in the URL parameter of your worksheet on Google Drive.

Then if you've exported all the environment variables manually.

```
nosetests
```

Or if you've set them in the `.env` file.

```
foreman run nosetests
```

## Improvements

- not hard code the Google login
