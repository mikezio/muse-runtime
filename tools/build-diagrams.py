#!/usr/bin/env python3
"""Build the repository's technical figures (standard library only).

Coordinates are intentionally explicit: each figure uses notation appropriate
for its subject, rather than a generic card layout. Rendering is optional and
not part of this generator. See docs/diagrams.md for scope and source notes.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse'

class Figure:
    def __init__(self, name, title, description, height, source):
        self.name, self.height = name, height
        self.parts = [f'''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(description)}</desc>
<metadata>{escape(source)}</metadata>
<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L8 4L0 8" fill="#222"/></marker></defs>
<style>text{{font-family:Arial,Helvetica,sans-serif;fill:#222;font-size:18px}}.title{{font-size:26px;font-weight:400}}.group{{font-size:19px;font-weight:700}}.small{{font-size:16px;fill:#555}}.mono{{font-family:Consolas,'Liberation Mono',monospace;font-size:16px}}.head{{font-size:18px;font-weight:700}}</style>
<rect width="960" height="{height}" fill="white"/>''']
        self.text(30, 42, title, 'title')
        self.line(30, 64, 930, 64, color='#bbb')

    def text(self, x, y, value, cls='', anchor='start'):
        self.parts.append(f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{escape(value)}</text>')

    def lines(self, x, y, values, cls='', anchor='start', gap=24):
        for i, value in enumerate(values):
            self.text(x, y+i*gap, value, cls, anchor)

    def rect(self, x, y, w, h, dashed=False, fill='white', weight=1.3):
        dash=' stroke-dasharray="6 4"' if dashed else ''
        self.parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="#333" stroke-width="{weight}"{dash}/>')

    def node(self, x, y, w, h, title, detail=None):
        self.rect(x,y,w,h)
        if detail is None:
            self.text(x+w/2,y+h/2+6,title,anchor='middle')
        else:
            self.text(x+w/2,y+27,title,'head','middle')
            for i,line in enumerate(detail):
                self.text(x+w/2,y+51+i*22,line,'small','middle')

    def line(self,x1,y1,x2,y2,arrow=False,dashed=False,color='#333',both=False):
        self.path(f'M{x1} {y1}H{x2}' if y1==y2 else f'M{x1} {y1}L{x2} {y2}',arrow,dashed,color,both)

    def path(self,d,arrow=False,dashed=False,color='#333',both=False):
        attrs=(' marker-end="url(#a)"' if arrow else '')+(' marker-start="url(#a)"' if both else '')+(' stroke-dasharray="5 4"' if dashed else '')
        self.parts.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.3"{attrs}/>')

    def note(self, text):
        self.text(30,self.height-23,text,'small')

    def save(self):
        (ROOT/'assets'/self.name).write_text('\n'.join(self.parts)+ '\n</svg>\n')

# Deployment diagram: containment denotes placement; arrows are selected interfaces.
f=Figure('architecture.svg','Muse deployment',
 'The personal VM contains a runtime cell and protected services outside that cell. The Hatch harness communicates with remote inference through a proxy. Clients connect to the harness. The diagram shows placement and selected interfaces, not every service connection.',
 740, SOURCE+'; published launch design, checked 2026-09-28. See docs/diagrams.md.')
f.text(30,105,'Outside the personal VM','group')
f.rect(295,90,635,595,weight=1.6)
f.text(315,120,'Personal cloud VM','group')
f.rect(315,145,595,225,dashed=True)
f.text(335,176,'Runtime cell · systemd-nspawn','group')
f.node(335,205,250,58,'hatch — agent harness')
f.node(335,302,250,44,'Shell and local CLIs')
f.line(460,263,460,302,True)
f.text(471,286,'executes','small')
f.lines(640,229,['/home/hatch','workspace and files'],'mono',gap=24)
f.lines(640,305,['/opt/hatch','shipped runtime'],'mono',gap=24)
f.node(30,205,210,58,'Web / mobile client')
f.line(240,234,335,234,True)
f.text(260,223,'chat','small')
f.text(335,414,'Protected services','group')
f.node(335,470,220,52,'Inference proxy')
f.path('M585 234H612V440H445V470',True,both=True)
f.text(455,430,'inference','small')
f.node(30,470,210,52,'Remote model serving')
f.line(335,496,240,496,True,both=True)
f.text(272,482,'I/O','small','middle')
f.line(605,448,605,659,color='#bbb')
f.lines(635,468,['Sentinel — action permissions','hatch-safety — inference checks','authd — credential service','privsep — connector workers','Browser broker','Postgres — application state'],cls='small',gap=33)
f.text(335,570,'Telemetry proxy','small')
f.text(335,620,'These services run outside the cell.','small')
f.note('Containment = deployment boundary. Arrows = selected interfaces. Published launch design; builds may differ.')
f.save()

# Logical sequence, not a second physical map.
f=Figure('request-lifecycle.svg','A tool-using conversation turn',
 'A client sends a message to the harness. The harness assembles context and calls inference. A tool request is executed and its result returns for further inference; this may repeat. The final reply goes to the client. Proxies and transport details are omitted.',
 740,'Logical sequence based on the runtime interfaces described in docs/02-the-agent-outside.md and docs/runtime-api.md.')
xs=[90,340,605,870]
for x,label in zip(xs,['Client','Harness','Model inference','Tool / service']):
 f.text(x,107,label,'head','middle');f.line(x,128,x,675,dashed=True,color='#999')
def message(a,b,y,label,returned=False):
 f.line(a,y,b,y,True,returned);f.text((a+b)/2,y-10,label,'small','middle')
message(90,340,157,'message')
f.rect(285,176,110,49,fill='#fafafa');f.lines(340,196,['assemble','context'],'small','middle',gap=19)
message(340,605,251,'inference request')
message(605,340,297,'tool request or final text',True)
f.rect(245,320,680,242,dashed=True)
f.text(258,345,'If a tool is requested; repeat as needed','small')
message(340,870,379,'route call · apply relevant authorization')
message(870,340,425,'tool result',True)
message(340,605,472,'next inference, including result')
message(605,340,522,'another tool request or final text',True)
message(340,90,612,'final reply',True)
f.text(340,656,'Asynchronous tools can return a receipt before a later handoff.','small')
f.note('Logical order only. Transport and proxies omitted; the tool loop is optional.')
f.save()

# Ownership tree: scheduled work is a separate activation lineage.
f=Figure('agent-tree.svg','Agent ownership',
 'A conversation root may delegate general children and own browser tasks. Further child delegation depends on policy. Scheduled, event-driven or queued work can activate a separate background worker with its own delivery path.',
 550,'Observed roles and native tool contracts, September 2026; see docs/15-agents.md.')
f.text(30,106,'Conversation work','group');f.text(690,106,'Background work','group')
f.line(650,95,650,482,color='#bbb')
f.node(175,140,280,60,'Conversation root')
f.node(30,282,245,65,'General subagent')
f.node(365,282,245,65,'Browser task agent')
f.path('M260 200V241H152V282',True);f.text(65,230,'delegates','small')
f.path('M375 200V241H487V282',True);f.text(430,230,'owns task','small')
f.node(30,416,245,55,'Further child')
f.line(152,347,152,416,True,dashed=True);f.text(168,389,'if allowed','small')
f.lines(385,394,['Self-contained brief;','browser-specific tools.'],'small')
f.node(690,140,240,70,'Schedule / event / queue')
f.node(690,282,240,65,'Background worker')
f.line(810,210,810,282,True);f.text(825,252,'activates','small')
f.node(690,416,240,55,'Configured delivery')
f.line(810,347,810,416,True);f.text(825,389,'reports','small')
f.note('Edges show ownership or activation, not shared context. Tools and model policy can differ by role.')
f.save()

# Browser lifecycle with explicit resume loop and separate session state.
f=Figure('browser-lineage.svg','Browser task lifecycle',
 'A submitted task is accepted, runs, and can complete or fail. A running task can wait for input or approval and resume under the same task. Session and authentication state belong to the browser service and are distinct from task state.',
 590,'Conceptual lifecycle from browser.spawn_task and browser.steer_task guidance; labels are not API state enums. See docs/06-browser.md.')
f.node(30,122,165,52,'Submitted');f.node(265,122,165,52,'Accepted');f.node(510,122,180,52,'Running');f.node(750,122,180,52,'Completed')
f.line(195,148,265,148,True);f.line(430,148,510,148,True);f.line(690,148,750,148,True)
f.node(370,300,230,60,'Waiting for input')
f.path('M555 174V235H485V300',True);f.text(315,221,'input / approval needed','small')
f.path('M600 330H655V174',True);f.lines(640,266,['steer / resume','same task'],'small','end')
f.node(740,300,190,60,'Failed')
f.path('M690 163H715V330H740',True);f.text(730,252,'error','small')
f.node(740,450,190,52,'Owner handoff')
f.path('M930 148H945V476H930',True);f.line(835,360,835,450,True)
f.line(30,398,680,398,color='#bbb')
f.text(30,436,'Browser session ≠ browser task','group')
f.lines(30,472,['Profile and authentication state are managed by the browser service.','A new task does not establish whether a login is present.','After interruption, inspect task status and effects before retrying.'],'small',gap=26)
f.note('Lifecycle is conceptual. Acceptance, completion and the owner receiving a result are separate events.')
f.save()

# Memory: several representations feed retrieval; no invented universal pipeline.
f=Figure('memory-pipeline.svg','Memory and later use',
 'Editable files, structured memory and indexes, and history/provenance are different representations. Relevant information is retrieved from supported surfaces and assembled into later context. Background upkeep and correction workflows vary by policy.',
 520,'Conceptual map of installed memory guidance and native schema/tool observations; see docs/12-memory.md.')
f.text(30,108,'Persistent representations','group')
f.rect(30,132,370,270,dashed=True)
f.lines(52,169,['Editable files'],'head');f.text(52,197,'Standing notes and preferences','small')
f.line(52,214,377,214,color='#bbb')
f.text(52,247,'Structured memory and indexes','head');f.text(52,275,'Claims, source links and retrieval data','small')
f.line(52,292,377,292,color='#bbb')
f.text(52,325,'History and provenance','head');f.text(52,353,'Conversation, task and correction records','small')
f.node(489,222,190,86,'Retrieve', ['relevant information'])
f.node(759,222,171,86,'Context', ['for later inference'])
f.line(400,265,489,265,True);f.line(679,265,759,265,True)
f.text(432,251,'read','small');f.text(696,251,'select','small')
f.text(30,448,'Correction and upkeep','head')
f.text(260,448,'Use the relevant stores and workflows; one file edit may be insufficient.','small')
f.note('Conceptual map, not a verified processing pipeline. Sources, indexes and maintenance vary by runtime policy.')
f.save()

# Scheduler has a real fan-in; waiting does not imply success or delivery.
f=Figure('scheduler-loop.svg','From trigger to delivery',
 'Schedules, events and queued work each feed eligibility and dispatch. A dispatched worker produces a run outcome. The runtime records it, then follows the configured delivery path. Waiting and interruptions require status checks rather than assumed success.',
 600,'Conceptual flow based on native scheduling/task guidance; see docs/11-scheduler.md.')
f.node(55,121,230,54,'Schedule due');f.node(365,121,230,54,'Event');f.node(675,121,230,54,'Queued work')
for x in [170,480,790]:f.line(x,175,x,220)
f.line(170,220,790,220);f.line(480,220,480,262,True)
f.node(355,262,250,58,'Eligibility / dispatch')
f.node(355,369,250,58,'Worker run');f.line(480,320,480,369,True)
f.node(35,369,245,58,'Waiting / interrupted');f.line(355,398,280,398,True)
f.lines(37,463,['Inspect current state.','Resume or retry only as appropriate.'],'small')
f.node(685,369,245,58,'Record run outcome');f.line(605,398,685,398,True);f.text(617,383,'ends','small')
f.node(685,478,245,58,'Configured delivery');f.line(807,427,807,478,True);f.text(823,458,'if applicable','small')
f.note('A job being defined, dispatched, completed and delivered are four different facts. No fixed cadence is implied.')
f.save()

# Table: independent control surfaces, not an override-precedence ladder.
f=Figure('configuration-layers.svg','Configuration surfaces',
 'Independent settings surfaces for files, reasoning, model selection, client flags, server rollout, action permissions and launch environment. Each has its own scope and evidence; the rows do not imply precedence.',
 705,'Observed configuration interfaces and limits, September 26–27, 2026. See docs/configuration.md and docs/feature-flags.md.')
f.text(30,112,'Surface','head');f.text(315,112,'Scope','head');f.text(615,112,'What can be verified','head');f.line(30,130,930,130)
rows=[
 ('Standing files',['Persona, notes, workflows'],['Relevant file / consumer behavior']),
 ('Reasoning preferences',['Root and subagent effort'],['Config API readback; provider-effective','effort was not exposed']),
 ('Model selection',['Global in the tested runtime'],['Selected route and diagnostic result;','switches cleared working context']),
 ('Client feature flags',['Web UI presentation / rollout'],['Client values, not all backend gates']),
 ('Server rollout / entitlement',['Backend feature availability'],['Supported capability or action result']),
 ('Action permissions',['Allowed action and its scope'],['Permission state / approval outcome']),
 ('Launch environment',['Service startup configuration'],['Protected effective state may be','unavailable from the cell'])]
for i,(name,scope,check) in enumerate(rows):
 y=162+i*72
 f.text(30,y,name);f.lines(315,y,scope,'small',gap=21);f.lines(615,y,check,'small',gap=21)
 f.line(30,y+43,930,y+43,color='#ccc')
f.note('Rows are independent surfaces, not an order of precedence. Stored intent and effective behavior can differ.')
f.save()

# One named authorization path, not a universal security flow.
f=Figure('trust-boundaries.svg','Example: authorizing an outbound request',
 'A cell process submits an outbound request to the egress proxy and Sentinel. The permission decision can allow, deny or ask the user through the client. An authorized credential-bearing request uses authd for credential insertion before reaching the service. Other tool paths differ.',
 725,SOURCE+'; schematic of the published egress path, not every tool or service. See docs/03-sentinel.md.')
f.text(30,112,'Request','group');f.text(332,112,'Authorization','group');f.text(730,112,'Other interfaces','group')
f.node(30,162,205,70,'Cell process',['outbound request'])
f.node(335,162,275,70,'Egress proxy / Sentinel',['evaluate action and scope'])
f.line(235,197,335,197,True)
f.node(730,162,200,70,'Muse client',['user approval'])
f.line(610,181,730,181,True);f.text(670,166,'ask','small','middle')
f.line(730,213,610,213,True,True);f.text(670,246,'decision','small','middle')
f.node(335,327,275,70,'Authorized request',['replace surrogates if needed'])
f.line(472,232,472,327,True);f.text(488,286,'allow','small')
f.node(30,327,205,70,'Blocked / error')
f.path('M335 217H306V362H235',True);f.text(263,296,'deny','small')
f.node(730,327,200,70,'authd',['credential service'])
f.line(610,350,730,350,True);f.line(730,378,610,378,True,True)
f.lines(666,427,['credential lookup / return','when required'],'small','middle',gap=22)
f.node(335,512,275,66,'External service')
f.line(472,397,472,512,True);f.text(488,479,'forward','small')
f.text(30,610,'Response path omitted. This is an authorization flow, not a deployment diagram.','small')
f.lines(30,657,['Cell UID 0 does not grant host authority. Authorized actions can still have consequences.','This example does not describe the distinct browser, privileged-worker or device paths.'],'small',gap=26)
f.save()
