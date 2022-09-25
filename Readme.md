# workouts-sheety-nutritionix

This project captures workout information in natural language and gets the details via an API

The APIs used are:

- Nutritionix API [docs](https://nutritionix.com)
- Sheety API [docs](https://sheety.co)

The nutritionix API is used to convert the natural language to the relevant form.

The extracted data are then fed into the Sheety API to save it in a Google Sheet.

This project uses:

- Python Functions: where all APIs are in a function.
- Loops: Where extracted data are processed and saved.
- Requests Module: To fetch request information

This project handles:

- API authentication
- API endpoint i.e. request and response processing.

