import dash
from dash import Input, Output, State, html, dcc, dash_table, MATCH, ALL, ctx
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, time, timedelta
import time as time_pck
import os
import dash_daq as daq

from app import app
import pages

server = app.server

#app.enable_dev_tools( dev_tools_ui=True, dev_tools_serve_dev_bundles=True, debug=True)

# start = 23
# end = 15

# def in_between(now, start, end):
#     if start <= end:
#         return start <= now < end
#     elif datetime.today().weekday() > 4:
#         return True
#     else: # over midnight e.g., 23:30-04:15
#         return start <= now or now < end


def create_main_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            direction='row',
            position='center',
            spacing=10,
            style={'margin-bottom':5},
            children=[
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=25,
                    radius=5,
                    color='indigo',
                    variant="filled",
                    style={'margin-left':10}
                ),
                dmc.Text(label, size="sm", color="gray", style={'font-family':'IntegralCF-Regular'}),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )

def create_accordianitem(icon, label, href):
    return dcc.Link(
        dmc.Group(
            direction='row',
            position='left',
            spacing=10,
            style={'margin-bottom':10},
            children=[
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=30,
                    radius=30,
                    color='indigo',
                    variant="light",
                ),
                dmc.Text(label, size="sm", color="gray", style={'font-family':'IntegralCF-Regular'}),
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )

app.layout = dmc.MantineProvider(
    id = 'dark-moder', 
    withGlobalStyles=True, 
    children = [
        html.Div(
            children = [

                # dcc.Interval(
                #     id='interval',
                #     n_intervals=0,
                #     interval=10*1000,
                # ),

                # html.Div(
                #     id = 'timer-sales-holder',
                #     style = {'display':'None'}
                # ),


                # dcc.Interval(
                #     id='minute-int',
                #     n_intervals=0,
                #     interval=2*1000,
                # ),

                dmc.Header(
                    height=70,
                    fixed=True,
                    pl=0,
                    pr=0,
                    pt=0,
                    style = {'background-color':'skyblue', 'color':'whitesmoke'},
                    children=[

                        # dmc.Container(
                        #     fluid=True,
                        #     pt=0,
                        #     pl=0,
                        #     pr=0,
                        #     children=[
                        #         dmc.Group(
                        #             id = 'style-1',
                        #             spacing=0,
                        #             position="left",
                        #             align="flex-start",
                        #             noWrap=True,
                        #             style={'overflow-x':'scroll', 'overflow-y':'hidden'},
                        #             children=[

                        #                 #])

                        #             ]
                        #         ),
                        #     ]
                        # ),

                        dmc.Container(
                            fluid=True,
                            children=[
                                dmc.Group(
                                    position="apart",
                                    align="center",
                                    children=[
                                        dmc.Center(
                                            children=[
                                                dcc.Link(
                                                    dmc.ThemeIcon(
                                                        html.Img(src= '..\\assets\\ibm_logo.png', style={'width':43}),
                                                        radius='sm',
                                                        size=44,
                                                        variant="filled",
                                                        color="blue",
                                                    ),
                                                    href=app.get_relative_path("/"),
                                                ),
                                                dcc.Link(
                                                    href=app.get_relative_path("/"),
                                                    style={"paddingTop": 2, "paddingLeft":10, "paddingBottom":5, "paddingRight":10, "textDecoration": "none"},
                                                    children=[
                                                        dmc.MediaQuery(
                                                            smallerThan="sm",
                                                            styles={"display": "none"},
                                                            children=[
                                                                dmc.Group(direction='column', align='center', spacing=0, position='center', children=[
                                                                    dmc.Text("Plotly Dash", size="lg", color="gray", style={'font-family':'IntegralCF-ExtraBold'}),
                                                                    dmc.Badge("2022 Holiday Challenge", variant="outline", color="blue", size="sm",  style={'margin-top':4})]
                                                                ) #leftSection=[html.Img(src='https://plotly.chiefs.work/ticketing/assets/Teams/NFL.svg',
                                                            ]
                                                        )
                                                    ]
                                                ),
                                                dmc.MediaQuery(
                                                    largerThan="sm",
                                                    styles={"display": "none"},
                                                    children=[
                                                        dmc.Group(direction='column', align='flex-start', spacing=0, position='center', 
                                                            children=[
                                                                dmc.Text("Plotly Dash", size="sm", color="gray", style={'font-family':'IntegralCF-ExtraBold'}),
                                                                dmc.Badge("2022 Holiday Challenge", variant="outline", color="red", size="xs")
                                                            ]
                                                        )
                                                    ]
                                                ),
                                            ]
                                        ),
                                        dmc.Group(
                                            direction = 'row',
                                            position="right",
                                            align="center",
                                            spacing="md",
                                            children=[
                                                html.Div(id = 'indicatorbox', className = 'indicator-box',
                                                    children=[
                                                        html.Div(id = 'indicatorpulse', className='indicator-pulse', children=[]),
                                                        html.Span(id = 'liveindicator', className= 'live-indicator', children=['LIVE']),
                                                        
                                                    ]
                                                ),
                                                html.A(
                                                    dmc.ThemeIcon(
                                                        DashIconify(icon = 'mdi:linkedin')
                                                    ),
                                                    href = 'https://www.linkedin.com/in/andrewschutte/',
                                                    target ='_blank'
                                                ),
                                                
                                                html.A(
                                                   dmc.ThemeIcon(
                                                        DashIconify(icon = 'mdi:twitter')
                                                    ), 
                                                    href = 'https://twitter.com/Andrewschutte2',
                                                    target ='_blank'
                                                ),

                                                html.A(
                                                    dmc.ThemeIcon(
                                                        DashIconify(icon = 'mdi:github'),
                                                        color = 'dark'
                                                    ),
                                                    href = 'https://github.com/almostBurtMacklin/Plotly-Challenge',
                                                    target ='_blank'
                                                )
                                            ],
                                        ),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
                dmc.Modal(
                    id = 'the-modal',
                    overflow = 'inside',
                    size = 'xl',
                    children = [
                        
                    ],
                    opened = False
                ),

                dmc.Navbar(
                    fixed=True,
                    width={"base": 300},
                    pl='sm',
                    pr='xs',
                    pt=0,
                    hidden=True,
                    hiddenBreakpoint='sm',
                    children=[
                        dmc.ScrollArea(
                            offsetScrollbars=True,
                            type="scroll",
                            children=[
                                dmc.Group(
                                    direction = 'column',
                                    align = 'center',
                                    position = 'center',\
                                    spacing = 'xs',
                                    children =[
                                        dmc.Text('Built By: Andrew Schutte', style = {'font-family':'IntegralCF-RegularOblique'}, size = 'sm'),
                                        dmc.Text('Kansas City, USA', style = {'font-family':'IntegralCF-RegularOblique'}, size = 'sm')
                                    ]
                                ),
                                
                                #html.Img(src='https://plotly.chiefs.work/ticketing/assets/SA.svg', id  = 'sa-logo', style={'width':160, 'margin-left':50}),
                                dmc.Divider(label='Customer Exploration', style={"marginBottom": 20, "marginTop": 5}),
                                dmc.Group(
                                    direction="column",
                                    children=[
                                        create_main_nav_link(
                                            icon="mdi:people-group",
                                            label="Customer Base",
                                            href=app.get_relative_path("/"),
                                        ),
                                        create_main_nav_link(
                                            icon="mdi:magnify",
                                            label="Churn Investigation",
                                            href=app.get_relative_path("/churn"),
                                        ),
                                        create_main_nav_link(
                                            icon="ooui:text-summary-ltr",
                                            label="Churn Prediction",
                                            href=app.get_relative_path("/summary"),
                                        ),
                                    ],
                                ),
                                # dmc.Divider(label='Ticket Sales', style={"marginBottom": 15, "marginTop": 10}),

                                # dmc.Group(
                                #     direction="column",
                                #     children=[
                                #         create_main_nav_link(
                                #             icon="mdi:people-group",
                                #             label="Single Game Sales",
                                #             href=app.get_relative_path("/singlegame-sales"),
                                #         ),

                                #         create_main_nav_link(
                                #             icon="bi:people",
                                #             label="New Season Ticket Sales",
                                #             href=app.get_relative_path("/newstm-sales"),
                                #         ),

                                #         create_main_nav_link(
                                #             icon="fa:refresh",
                                #             label="Renewal",
                                #             href=app.get_relative_path("/renewal"),
                                #         ),
                                #         create_main_nav_link(
                                #             icon="material-symbols:sports-football-rounded",
                                #             label="Playoffs",
                                #             href=app.get_relative_path("/playoff_tickets"),
                                #         ),
                                #     ]
                                # ),

                                # dmc.Divider(style={"marginBottom": 0, "marginTop": 10}),

                                # dmc.Accordion(
                                #     #iconPosition='right',
                                #     multiple=True,
                                #     style={'font-family':'IntegralCF-Regular'},
                                #     children=[
                                #         dmc.AccordionItem(
                                #             icon=[DashIconify(icon='bi:people', width=18)],
                                #             label="Sales Rep Tracking",
                                #             children=[
                                #                 create_accordianitem(
                                #                     icon="iconoir:leaderboard-star",
                                #                     label="Sales Leaderboard",
                                #                     href=app.get_relative_path("/salesrep-leaderboard"),
                                #                 ),
                                #                 create_accordianitem(
                                #                     icon="iconoir:leaderboard-star",
                                #                     label="Deposit Leaderboard",
                                #                     href=app.get_relative_path("/salesrep-deposits"),
                                #                 ),
                                #             ]
                                #         ),
                                #         dmc.AccordionItem(
                                #             icon=[DashIconify(icon='bx:party', width=18)],
                                #             label="Season Ticket Member Events",
                                #             children=[

                                #                 create_accordianitem(
                                #                     icon="fa:refresh",
                                #                     label="Draft Fest",
                                #                     href=app.get_relative_path("/stmevents-draftfest"),
                                #                 ),

                                #                 create_accordianitem(
                                #                     icon="fluent:tent-16-filled",
                                #                     label="Training Camp",
                                #                     href=app.get_relative_path("/stmevents-training-camp"),
                                #                 ),

                                #             ]
                                #         ),
                                #         dmc.AccordionItem(
                                #             icon=[DashIconify(icon='bi:file-earmark-bar-graph', width=18)],
                                #             label="Reporting",
                                #             children=[
                                #                 create_accordianitem(
                                #                     icon="fa:refresh",
                                #                     label="Box Office",
                                #                     href=app.get_relative_path("/reporting-boxoffice"),
                                #                 ),
                                #             ]
                                #         ),
                                #     ],
                                # ),
                            ],
                        )
                    ],
                ),

                dcc.Location(id='url'),
                dmc.MediaQuery(
                    largerThan="xs",
                    styles={'height':'100%', 'margin-left':'300px', 'margin-top':70},
                    children = [
                        html.Div(
                            id='content',
                            style={'margin-top':'70px'}
                        )
                    ],
                ),
            ]
        )
    ]
)

#analytics = dash_user_analytics.DashUserAnalytics(app, automatic_routing=False)

@app.callback(Output('content', 'children'),
                [Input('url', 'pathname')])
def display_content(pathname):
    page_name = app.strip_relative_path(pathname)
    if not page_name:  # None or ''
        return pages.customerbase.layout
    elif page_name == 'churn':
        return pages.churn.layout
    elif page_name == 'summary':
        return pages.summary.layout
    # elif page_name == 'pricing':
    #     return pages.pricing.layout
    # elif page_name == 'revenueprediction':
    #     return pages.revenueprediction.layout
    # elif page_name == 'stmevents-training-camp':
    #     return pages.training_camp.layout
    # elif page_name == 'salesrep-leaderboard':
    #     return pages.salesrep.layout
    # elif page_name == 'reporting-boxoffice':
    #     return pages.boxoffice.layout
    # elif page_name == 'salesrep-deposits':
    #     return pages.season_ticket_deposits.layout
    # elif page_name == 'renewal':
    #     return pages.renewal.layout
    # elif page_name == 'playoff_tickets':
    #     return pages.playoff_tickets.layout
    # elif pathname.endswith('/_analytics'):
    #     return analytics.display_analytics()

# @app.callback(Output('user-tooltip', 'label'), 
#               Output('user-label', 'children'),
#               Output('user-headshot', 'src'),
#               Input('interval', 'n_intervals'))

# def update_userinfo(n):

#     username = str(auth.get_username())

#     headshot = 'https://plotly.chiefs.work/ticketing/assets/Headshots/'+str(username)+'.png'

#     return username, username, headshot

# @app.callback(Output('style-1', 'children'),
#               Input('interval', 'n_intervals'))

# def update_header(n):

#     df = pd.read_feather('/data/2022alltickets.feather')
#     dfseason = pd.read_excel('/data/2022Season.xlsx', engine='openpyxl')

#     games = ['PR01', 'PR02', 'LAC', 'LVR', 'BUF', 'TEN', 'JAC', 'LAR', 'SEA', 'DEN']

#     children=[]

#     for i in games:

#         date = dfseason[dfseason['event_name']=='22GM'+str(i)]['event_date'].iloc[0]
#         time = dfseason[dfseason['event_name']=='22GM'+str(i)]['event_time'].iloc[0]

#         seats = '{:,.0f}'.format(df[df['event_name']=='22GM'+str(i)]['num_seats'].sum())
#         rev = '${:,.0f}'.format(df[df['event_name']=='22GM'+str(i)]['block_purchase_price'].sum())

#         children.append(
#             dmc.Paper(
#                 withBorder=True,
#                 style={'height':'60px', 'width':'200px'},
#                 pl=2,
#                 pr=2,
#                 pb=2,
#                 children=[
#                     dmc.Group(direction='row', align='center', position='apart', style={}, children=[
#                         html.Img(src='assets/Teams/'+str(i)+'.svg', style={'height':'15px'}),
#                         dmc.Group(direction='row', position='apart', align='center', spacing=5, children=[
#                             dmc.ActionIcon(DashIconify(icon="clarity:details-line"), id = {'type':'ActionIcon', 'index': i}, color="blue", size=15, variant="hover"),
#                             dmc.Text(str(date)+' | '+str(time), weight='bold', color='dimmed', style={'fontSize':'10px', 'margin':0}),
#                             #html.Img(src=app.get_asset_url('/Broadcast/FOX_BLACK.svg'), style={'height':'10px', 'margin-top':0, 'padding':0}),
#                         ])
#                     ]),

#                     dmc.Group(direction='column', position='center', spacing=0, style={'margin-bottom':'0px'}, children=[
#                         dmc.Text('Tickets: '+str(seats), weight='bold', style={'fontSize':'11px'}),
#                         dmc.Text('Revenue: '+str(rev), weight='bold', style={'fontSize':'11px'}),
#                     ]),

#                     dmc.Group(direction='row', position='apart', align='center', children=[
#                         #html.Img(src=app.get_asset_url('/Broadcast/FOX_BLACK.svg'), style={'height':'10px', 'margin-top':0}),
#                     ])

#                 ]
#             ),
#         )

#     return children

# @app.callback(
#     Output("the-modal", "opened"),
#     Output("the-modal", 'title'),
#     Output('the-modal', 'children'),
#     Input({'type':'ActionIcon', 'index':ALL}, "n_clicks"),
#     State("the-modal", "opened"),
#     prevent_initial_call=True,
# )
# def modal_demo(nc1, opened):

#     clicked_game = ctx.triggered_id['index']
#     #print(nc1)

#     if not any(nc1):
#         return dash.no_update, dash.no_update, dash.no_update
#     else:
#         gm = '22GM' + str(clicked_game)
#         df = pd.read_feather('/data/2022alltickets.feather')#.query('event_name == @gm')
#         dfseason = pd.read_excel('/data/2022Season.xlsx', engine='openpyxl')
#         date = dfseason[dfseason['event_name']=='22GM'+str(clicked_game)]['fancy_date'].iloc[0]
#         time = dfseason[dfseason['event_name']=='22GM'+str(clicked_game)]['event_time'].iloc[0]
#         broadcast = dfseason[dfseason['event_name']=='22GM'+str(clicked_game)]['broadcast'].iloc[0]
#         color = dfseason[dfseason['event_name']=='22GM'+str(clicked_game)]['color'].iloc[0]

#         rev = '${:,.0f}'.format(df[df['event_name']==gm]['block_purchase_price'].sum())
#         atp = '${:,.0f}'.format((df[df['event_name']==gm]['block_purchase_price'].sum())/(df[(df['event_name']==gm) & (df['comp_name']=='Not Comp')]['num_seats'].sum()))
#         seats = '{:,}'.format(df[(df['event_name']==gm) & (df['comp_name']=='Not Comp')]['num_seats'].sum())
#         comp = '{:,}'.format(df[(df['event_name']==gm) & (df['pc2']=='C')]['num_seats'].sum())
#         dist = '{:,}'.format(df[df['event_name']==gm]['num_seats'].sum())


#         df_secondary = pd.read_feather('/data/resale2022.feather')
#         dfactive = df_secondary[df_secondary['ticket_status'].isin(['Active', 'Posted for Resale'])]

#         resale = '{:,}'.format(dfactive[dfactive['event_name']=='22GM'+str(clicked_game)]['num_seats'].sum())

#         modal_header = [
#            dmc.Group(
#                 position = 'center',
#                 direction = 'row',
#                 spacing = 'sm',
#                 grow = True,
#                 #style={'font-family':'IntegralCF-RegularOblique'},
#                 children = [
#                     html.Img(src='assets/Teams/'+str(clicked_game)+'.svg', style = {'height':'50px', 'margin-left':'auto', 'margin-right':'auto', 'display':'block'}),
#                     dmc.Text(str(date), size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique', 'text-align':'center'}),
#                     dmc.Text(str(time), size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique', 'text-align':'center'}),
#                     html.Img(src='assets/Broadcast/'+ broadcast, style = {'height':'45px', 'margin-left':'auto', 'margin-right':'auto', 'display':'block'}),
                    
#                     ]
#                     ), 
#         ]


#         modal_child = [
            
#             dmc.SimpleGrid(
#                 cols = 2,
#                 style = {'text-align':'center'},
#                 children = [
#                     dmc.Paper(
#                         radius="md", # or p=10 for border-radius of 10px
#                         withBorder=True,
#                         shadow='xs',
#                         p='sm',
#                         #style={'height':'175px'},
#                         children=[
#                             dmc.Center(
#                                 dmc.ThemeIcon(
#                                     size=50,
#                                     radius="xl",
#                                     #color=color,
#                                     variant="light",
#                                     style = {'color':color},
#                                     children=[DashIconify(icon="ant-design:dollar-circle-filled", width=30)]
#                                 )
#                             ),
#                             dmc.Group(
#                                 direction='column',
#                                 position='center',
#                                 spacing='xs',
#                                 style={'margin-top':10},
#                                 children=[
#                                     dmc.Text('Total Game Revenue', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
#                                     dmc.Text(rev, size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
#                                     dmc.Text('+ $ Today', size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
#                                     ]
#                                 )
#                             ],
#                         ),
#                     dmc.Paper(
#                         radius="md", # or p=10 for border-radius of 10px
#                         withBorder=True,
#                         shadow='xs',
#                         p='sm',
#                         #style={'height':'175px'},
#                         children=[
#                             dmc.Center(
#                                 dmc.ThemeIcon(
#                                     size=50,
#                                     radius="xl",
#                                     #color=color,
#                                     variant="light",
#                                     style = {'color':color},
#                                     children=[DashIconify(icon="carbon:chart-average", width=30)]
#                                 )
#                             ),
#                             dmc.Group(
#                                 direction='column',
#                                 position='center',
#                                 spacing='xs',
#                                 style={'margin-top':10},
#                                 children=[
#                                     dmc.Text('Average Ticket Price', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
#                                     dmc.Text(atp,  size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
#                                     dmc.Text('+ $ Today',  size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
#                                     ]
#                                 )
#                             ],
#                         ),dmc.Paper(
#                         radius="md", # or p=10 for border-radius of 10px
#                         withBorder=True,
#                         shadow='xs',
#                         p='sm',
#                         #style={'height':'175px'},
#                         children=[
#                             dmc.Center(
#                                 dmc.ThemeIcon(
#                                     size=50,
#                                     radius="xl",
#                                     #color=color,
#                                     variant="light",
#                                     style = {'color':color},
#                                     children=[DashIconify(icon="majesticons:ticket-text", width=30)]
#                                 )
#                             ),
#                             dmc.Group(
#                                 direction='column',
#                                 position='center',
#                                 spacing='xs',
#                                 style={'margin-top':10},
#                                 children=[
#                                     dmc.Text('Total Tickets Sold', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
#                                     dmc.Text(seats ,size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
#                                     dmc.Text('+ $ Today', size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
#                                     ]
#                                 )
#                             ],
#                         ),
                        
#                         dmc.Paper(
#                         radius="md", # or p=10 for border-radius of 10px
#                         withBorder=True,
#                         shadow='xs',
#                         p='sm',
#                         #style={'height':'175px'},
#                         children=[
#                             dmc.Center(
#                                 dmc.ThemeIcon(
#                                     size=50,
#                                     radius="xl",
#                                     #color=color,
#                                     variant="light",
#                                     style = {'color':color},
#                                     children=[DashIconify(icon="ic:round-view-compact", width=30)]
#                                 )
#                             ),
#                             dmc.Group(
#                                 direction='column',
#                                 position='center',
#                                 spacing='xs',
#                                 style={'margin-top':10},
#                                 children=[
#                                     dmc.Text('Total Tickets Comped', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
#                                     dmc.Text(comp, size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
#                                     dmc.Text('+ $ Today', size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
#                                     ]
#                                 )
#                             ],
#                         ),

#                         dmc.Paper(
#                         radius="md", # or p=10 for border-radius of 10px
#                         withBorder=True,
#                         shadow='xs',
#                         p='sm',
#                         #style={'height':'175px'},
#                         children=[
#                             dmc.Center(
#                                 dmc.ThemeIcon(
#                                     size=50,
#                                     radius="xl",
#                                     #color=color,
#                                     variant="light",
#                                     style = {'color':color},
#                                     children=[DashIconify(icon="majesticons:ticket-check", width=30)]
#                                 )
#                             ),
#                             dmc.Group(
#                                 direction='column',
#                                 position='center',
#                                 spacing='xs',
#                                 style={'margin-top':10},
#                                 children=[
#                                     dmc.Text('Total Tickets Distributed', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
#                                     dmc.Text(dist, size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
#                                     dmc.Text('+ $ Today',  size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
#                                     ]
#                                 )
#                             ],
#                         ),

#                          dmc.Paper(
#                         radius="md", # or p=10 for border-radius of 10px
#                         withBorder=True,
#                         shadow='xs',
#                         p='sm',
#                         #style={'height':'175px'},
#                         children=[
#                             dmc.Center(
#                                 dmc.ThemeIcon(
#                                     size=50,
#                                     radius="xl",
#                                     #color=color,
#                                     variant="light",
#                                     style = {'color':color},
#                                     children=[DashIconify(icon="majesticons:tickets", width=30)]
#                                 )
#                             ),
#                             dmc.Group(
#                                 direction='column',
#                                 position='center',
#                                 spacing='xs',
#                                 style={'margin-top':10},
#                                 children=[
#                                     dmc.Text('Total Resale Tickets Available', size='xs', color='dimmed', style={'font-family':'IntegralCF-RegularOblique'}),
#                                     dmc.Text(resale, size='xl', style={'font-family':'IntegralCF-ExtraBold'}),
#                                     dmc.Text('+ $ Today',  size='xs', color='green', style={'font-family':'IntegralCF-RegularOblique'})
#                                     ]
#                                 )
#                             ],
#                         ),
#                 ]

#             )
                
#         ]

#         #print(rev, atp, seats, comp,dist)

#         return not opened, modal_header, modal_child


# @app.callback(Output('hidden-revenue-comp', 'label'),
#                 Input('interval', 'n_intervals'))
# def update_tooltip(n):
#     df = pd.read_csv('/data/comp-revenue.csv')

#     comp_rev = int(df.comp_rev.iloc[0])

#     dfall_rev = pd.read_feather('/data/singlegame22.feather')

#     totaltd = int(dfall_rev['block_purchase_price'].sum())

#     totaltdf = '${:,.0f}'.format(totaltd + comp_rev)

#     return totaltdf


# @app.callback(Output('dark-moder', 'theme'),
#             Output('sa-logo', 'src'),
#             Input('interval', 'n_intervals'))
# def updating_darkmode(val):

#     tod = "night" if in_between(datetime.now().time(), time(start), time(end)) else "day"

#     if tod == 'night':
#         return {"colorScheme":"dark"}, 'https://plotly.chiefs.work/ticketing/assets/SA_darkmode.svg'
#     else:
#         return {}, 'https://plotly.chiefs.work/ticketing/assets/SA.svg'

@app.callback([Output(component_id='liveindicator', component_property='className'),
              Output(component_id='indicatorpulse', component_property='className')],
             [Input(component_id='interval', component_property='n_intervals')])

def update_indicator(n):

    # if (os.path.getmtime('/data/live_sales_22.feather') - time_pck.time()) < -60:
    #     return 'live-indicator-off', 'indicator-pulse-off'
    # else:
    return 'live-indicator', 'indicator-pulse'

# @app.callback(Output('timer-sales', 'children'),
#             Input('minute-int', 'n_intervals'),
#             prevent_initial_call=True)
# def update_timer(val):
#     df = pd.read_csv('/data/last_sale.csv')
#     t_event = df['add_datetime'].iloc[0]
#     #t_event = '2021-08-08 00:00:00.00'
#     t_current = (datetime.now()- timedelta(hours=6))
#     event_time_obj = datetime.strptime(t_event, '%Y-%m-%d %H:%M:%S.%f')
#     delta = t_current - event_time_obj
#     #deltaseconds = delta.total_seconds()
#     secondsx = delta.total_seconds()

#     #hours = int(secondsx // 3600)
#     minutes = "{:02d}".format(int((secondsx) // 60))
#     seconds = "{:02d}".format(int(secondsx % 60))

#     time = "{}:{}".format(minutes,seconds)

#     return time    

if __name__ == '__main__':
    app.run_server(debug=True)
