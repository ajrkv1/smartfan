# smartfan

A flask REST api for controlling the radio-controlled ceiling fan in my room using rpitx and recorded signals

## Dependencies

The requirements for the REST-API are [flask](https://flask.palletsprojects.com/en/2.1.x/) and [flask_restful](https://flask-restful.readthedocs.io/en/latest/). For the transmitter module the [rpitx](https://github.com/F5OEO/rpitx) is used. to record the iq files I used an [rtl_sdr](https://rtl-sdr.com). 

## Deployment

This is only a flask app. to run it outside of the flask development server you will need to use other programs, to manage TLS connections and logs.

## Security

**DONT USE THIS APPLICATION WITHOUT A SECURE CONNECTION**. Otherwise just about anyone would be able to use this just from inside your network (or from the internet if your app is portforwarded). Use a secure TLS connection.