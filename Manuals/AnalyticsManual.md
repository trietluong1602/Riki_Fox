# Analytics Feature Manual

## Table of Contents
1. [Tracking Page Views](#tracking-page-views)
2. [Viewing Page View Counts](#viewing-page-view-counts)
3. [Analyzing Page View Timestamps](#analyzing-page-view-timestamps)

## Tracking Page Views <a name="tracking-page-views"></a>

Whenever a content page is visited, a POST request is sent to the `/track_page_view` route, with the page name as the request body. This will increment the view count for the specified page and record a timestamp for the view, both actions taking place in the SQLite database.

## Viewing Page View Counts <a name="viewing-page-view-counts"></a>

To view the total view count for a page, press the "View Analytics" button on the side bar of a page. 

A POST request to the `/get_view_count` route with the page name in the request body. This will return and therefore display the total view count for the specified page.

## Analyzing Page View Timestamps <a name="analyzing-page-view-timestamps"></a>

This can also be viewed from the "View Analytics" popup. A POST request is sent to the `/get_timestamps` route with the page name in the request body. This will return a list of timestamps and the count of views for each timestamp for the specified page. This will then be passed into a Chart.js for formatting into a bar graph, before being displayed on the screen.
