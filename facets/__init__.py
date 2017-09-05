#!/usr/bin/env python
# coding=utf-8

from facets.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator
import base64

model_href = "facets-jupyter.html"


def get_facets_overview(dataframes):
    '''
    Get html of facets-overview
    Argument:
        dataframes: [{'name': 'nameX', 'table': tableX}, ...]
                    tableX is the dataframe from pandas
    Return:
        html: html to display(You can use display(HTML(html)) to display it in notebook)
    '''
    gfsg = GenericFeatureStatisticsGenerator()
    proto = gfsg.ProtoFromDataFrames(dataframes)
    protostr = base64.b64encode(proto.SerializeToString()).decode('utf-8')
    HTML_TEMPLATE = """
        <link rel="import" href="{model_href}" >
        <facets-overview id="elem"></facets-overview>
        <script>
          document.querySelector("#elem").protoInput = "{protostr}";
        </script>
    """
    html = HTML_TEMPLATE.format(protostr=protostr, model_href=model_href)
    return html


def get_facets_dive(data):
    '''
    Get html of facets-dive
    Argument:
        data: is the dataframe from pandas
    Return:
        html: html to display(You can use display(HTML(html)) to display it in notebook)
    '''
    jsonstr = data.to_json(orient='records')
    HTML_TEMPLATE = """
        <link rel="import" href="{model_href}">
        <facets-dive id="elem" height="600"></facets-dive>
        <script>
          var data = JSON.parse('{jsonstr}');
          document.querySelector("#elem").data = data;
        </script>
    """
    html = HTML_TEMPLATE.format(jsonstr=jsonstr, model_href=model_href)
    return html
