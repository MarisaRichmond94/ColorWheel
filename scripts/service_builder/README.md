# Service Builder
**The service builder is a templating script designed to generate 80-95% of the code needed to create a generic RESTful Python service.**

## How To Run It

1) Navigate to the `/api` or `/restful_services` folder:

2) Run the following command

`python {path/to/script/folder/main.py} -p {service_name_plural} -s {service_name_singular} -t {table_type} -m [...methods]`

Example (starting from the /api folder): `python devops/service_builder/main.py -p potatoes -s potato -t dim -m POST GET_BY_ID DELETE_BY_ID`

3) A new service by the `plural-service-name` will be generated in the `/restful_services` folder and a new table database model will be generated in the `/db_models` folder

## Required Inputs

| <div style="min-width:190px">Flag</div> | Description | Options |
| --- | --- | --- |
| `-p`,<br>`--plural-service-name` | Plural name of the service |
| `-s`,<br>`--singular-service-name` | Singular name of the service |
| `-t`,<br>`--table-type` | Type of table | dim, fct |
| `-m`,<br>`--methods`,<br>`--all` | API methods to create. Options only required for `--methods` | POST, GET, GET_BY_ID, PATCH, DELETE, DELETE_BY_ID |

## Optional Inputs

| <div style="min-width:130px">Flag</div> | Description |
| --- | --- |
| `--foreign-dims` | (fct table only, otherwise ignored)<br>The foreign dimensions that should be associated with the table/service as comma separated strings giving the plural/singular service name |
| `--dimensions` | The dimensions that should be associated with the table/service, listing the key, sqlalchemy type, generic type, whether or not the dimension is required, and whether or not the dimension must be unique as a comma separated string |
| `--method-args` | (only applicable to `GET`, `PATCH` and `DELETE` methods)<br>The args required for each method |

Examples

 `--foreign-dims content_items,content_item,dim tags,tag,dim`

`--dimensions name,String,str,True,True order_index,Integer,int,False,False`

`--method-args get,name patch,name,order_index delete,group`
