# Test Engineering Portfolio
This portfolio showcases two test automation projects:
1. **API test suite:** API test cases created for the
[Restful-Booker API](https://restful-booker.herokuapp.com/) using Python 3.
This can be found in the [api_testing](https://github.com/dervent/qa_portfolio/tree/master/api_testing) directory.
2. **Selenium test suite:** TBA.

## Committing Code
This project uses git hook scripts to perform static analysis of code to be committed.
These steps assume you have Python 3.8 installed.
1. Install project requirements : `pip3 install -r requirements.pip`.
2. Run `pre-commit install` to set up the hook scripts.
3. Now, whenever a commit is made, `pre-commit` will automatically run using the hooks 
defined in the _.pre-commit-config.yaml_ file found in the root directory of this repository.
