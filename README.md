# pytorch_config_utils
config utils for pytorch


config control module via yaml.

It takes a dictionary as an input and can be used like a class.

ex) Existing: a = config['loss_weight']

Current: a = config.loss_weight

In the past, there were many modules that did not provide nested modifications.

However, this module provides nested modifications.

ex) config.content_loss.loss_weight = 7
