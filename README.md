# stripe-errors-translations
WiP french translations for Stripe errors and end-users messages

Shared MIT licensed because the original error texts can be found in the also MIT licensed Stripe API.

Litteral error messages and french translations are in the `litterals` directory.
User-friendly messages compatible with those error codes can be found in the `enduser` directory.

Some error codes shouldn't be reported as is to the client, as they could leak information (e.g. when a card is lost, Stripe recommends to show a generic error message instead). Those cases are available in the `opaque.json` file with error codes to send instead.

The WiP `generate.py` file allows you to generate error codes for your front end.
