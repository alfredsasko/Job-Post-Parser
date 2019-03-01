# job posting data model objects and sets

# import libraries
import csv

# modul constants
# set of programming tools
def _generate_toolset(fname = 'programming-languages.csv' ):
    TOOL_SET = set()
    with open(fname, newline = '') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tool = row['name'].lower()
            TOOL_SET.add(tool)
    return TOOL_SET

TOOL_SET = _generate_toolset()
print(TOOL_SET)

# set of job maturity levels
MATURITY_LEVELS = set(('junior', 'mature', 'senior'))

# set of data science job job types
# data analyst   - junior - basic exploratory data analysis and reporting
# data engineer  - mature - set up complex data-structures,
#                           need for strong software engineering skills
# ml engineer    - senior - producing data driven products and
#                           less answering operational questions
# data scientist - senior - generalist who can do everything focused on
#                           big data, messy 'real life' datasets
#                           with certain niche like functional, ml etc...
JOB_TYPES = set(('data analyst', 'data engineer', 'ml engineer', \
                 'data scientist'))

# data model objects
class Industry:
    # Industry table
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Company:
    # company table
    def __init__(self, id, name, industry_id):
        self.id = id
        self.name = name
        self.industry_id = industry_id

class JobType:
    # job type table
    def __init__(self, id, type_):
        if type in JOB_TYPES:
            self.id = id
            self.type_ = type_
        else:
            pass # raise exception: not allowed job type

class JobMaturity:
    # job manturity table
    def __init__(self, id, level):
        if level in MATURITY_LEVELS:
            self.id = id
            self.level = level
        else:
            pass # raise exception: not allowed level

class SwTool:
    # programming languages (software tool) table
    def __init__(self, id, name):
        if  name in TOOL_SET:
            self.id = id
            self.name = name
        else:
            pass # raise exception: not allowed tool

class JobPost:
    # job posting table
    def __init__(self, id, title, min_salary, requirements, responsibilities, \
                company_id, job_maturity_id, job_type_id):
        self.id = id
        self.title = title
        self.min_salary = min_salary
        self.requirements = requirements
        self.responsibilities = responsibilities
        self.company_id = company_id
        self.job_maturity_id = job_maturity_id
        self.job_type_id = job_type_id

class JobTool:
    # conjuction table to realize many to many relationship
    # between software tool and job posting table
    def __init__(self, id, job_post_id, sw_tool_id):
        self.id = id
        self.job_post_id = job_post_id
        self.sw_tool_id = sw_tool_id

# exception classes for data model constraints
class Error(Exception):
    # base class for exceptions in this module
    pass

class ToolSetError(Error):
    # exception raised for tools not in TOOL_SET
    # attributes:
    # tool - tool not it TOOL_SET
    # message - explanation of the error
    def __init__(self, tool, message):
        self.tool = tool
        self. message = message

class JobMaturityError(Error):
    # exception raised for job maturity level not in MATURITY_LEVELS
    # attributes:
    # level - job maturity level not in MATURITY_LEVELS
    # message - explanation of the error
    def __init__(self, level, message):
        self.level = level
        self. message = message

class JobTypeError(Error):
    # exception raised for job type not in JOB_TYPES
    # attributes:
    # type - job type not in JOB_TYPES
    # message - explanation of the error
    def __init__(self, job_type, message):
        self.type_ = level
        self. message = message
