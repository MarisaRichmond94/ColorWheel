# Service Builder
**The service builder is a templating script designed to generate 80-95% of the code needed to create a generic RESTful Python service using our team's current standards.**

## How To Run It

1) Navigate to the `/api` or `/restful_services` folder:

2) Run the following command

`python {path/to/script/folder/main.py} --service_name_plural {service_name_plural} --service_name_singular {service_name_singular} --table_type {table_type} --methods [...methods]`

Example (starting from the /api folder): `python devops/service_builder/main.py --service_name_plural potatoes --service_name_singular potato --table_type dim --methods POST GET_BY_ID DELETE_BY_ID`

3) A new service by the `service_name_plural` will be generated in the `/restful_services` folder and a new table database model will be generated in the `/db_models` folder

## Available Inputs

Available `methods` include POST, GET, GET_BY_ID, PATCH, DELETE, and DELETE_BY_ID (must be in all caps); however, you can use `--all` to generate all method types

Available `table_types` include dim and fct

## Optional Inputs

There are 3 more optional inputs:

1) `--foreign-dims` - (fct table only, otherwise ignored) The foreign dimensions that should be associated with the table/service as comma separated strings giving the plura/singular service name

example: `--foreign-dims content_items,content_item tags,tag`

2) `--dimensions` - The dimensions that should be associated with the table/service, listing the key, sqlalchemy type, generic type, whether or not the dimension is required, and whether or not the dimension must be unique as a comma separated string

example: `--dimensions name,String,str,True,True order_index,Integer,int,False,False`

3) `--method-args` - The args required for each method (only applicable to `Get`, `PATCH` and `DELETE` methods)

example: `--method-args get,name patch,name,order_index delete,group`
