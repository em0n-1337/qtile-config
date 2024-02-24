from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
import subprocess

modkey = "mod4"
mod = "mod1"
terminal = guess_terminal()
dmenu_cmd="/home/emon/.config/suckless/dmenu/dmenu_run -l 10 -nb '#0a0f09' -nf '#ffffff' -sb '#2f3328'"

keys = [

    #############################
    ##### SWITCH BETWEEN WINDOWS
    #############################
    Key([mod], "k", lazy.layout.next(), desc="Move window focus to other window"),


    #############################
    ##### COLUMN
    #############################
    # Key([mod], "h", lazy.layout.grow_left()),
    # Key([mod], "l", lazy.layout.grow_right()),
    # Key([mod], "m", lazy.layout.swap_column_left()),


    #############################
    ##### MONADTALL
    #############################
    Key([mod], "h", lazy.layout.shrink_main()),
    Key([mod], "l", lazy.layout.grow_main()),
    Key([mod], "m", lazy.layout.swap_main()),


    #############################
    ##### MONADWIDE
    #############################
    Key([mod], "n", lazy.layout.grow()),
    Key([modkey], "k", lazy.layout.up()),
    Key([modkey], "j", lazy.layout.down()),
    Key([modkey], "h", lazy.layout.left()),
    Key([modkey], "l", lazy.layout.right()),
    Key([mod, "shift"], "n", lazy.layout.shrink()),
    Key([mod, "shift"], "u", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "d", lazy.layout.shuffle_down()),


    #############################
    ####### SPAWN APPLICATIONS
    #############################
    Key([mod, "shift"], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "p", lazy.spawn(dmenu_cmd)),


    #############################
    ####### OTHERS
    ############################
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod], "d", lazy.next_layout()),
    Key([mod], "i", lazy.prev_layout()),

]

# WAYLAND KEYS
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )

groups = [
    Group('1', label=""),
    Group('2', label=""),
    Group('3', label=" "),
    Group('4', label=""),
    Group('5', label=" "),
    Group('6', label=" "),
    Group('7', label=" "),
    Group('8', label=""),
    Group('9', label=""),
]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),

            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    # layout.Columns(
    #     border_focus='#9db548',
    #     border_normal='#141414',
    #     border_on_single=True,
    #     split=True,
    #     border_width=1,
    #     margin = 4,
    # ),
    layout.MonadTall(
        border_focus='#9db548',
        border_normal='#141414',
        border_width=1,
        single_border_width=1,
        single_margin=4,
        margin = 4,
    ),
    layout.MonadWide(
        border_focus='#9db548',
        border_normal='#141414',
        border_width=1,
        margin=4,
        single_border_width=1,
        single_margin=4,
    ),
    layout.Max(
        border_focus='#9db548',
        border_normal='#141414',
        border_width=1,
        margin = 4,
    ),
]

widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=0,
)
extension_defaults = widget_defaults.copy()

win_sep = '#453f1d'

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    borderwidth = 0,
                    font = 'sans',
                    fontsize = 15,
                    padding_x = 0,
                    active = '#a4ba34',
                    inactive = '#b1b5b3',
                    #urgent_text = '#c25c34',
                    highlight_method = 'line',
                    highlight_color = ['#000000', '#494d42'],
                    disable_drag = True,
                    center_aligned = True,
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 20,
                    foreground = win_sep,
                ),
                
                widget.CurrentLayout(
                    font = 'ComicShannsMonoNerdFont',
                    fontsize = 14,
                    foreground = '#b8b43b',
                    center_aligned = True,
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 20,
                    foreground = win_sep,
                ),
                
                widget.WindowName(
                    font = 'ComicShannsMonoNerdFont',
                    fontsize = 13,
                    foreground = '#c7c7c7',
                    format = "{name}",
                    center_aligned = True,
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 20,
                    foreground = win_sep,
                ),

                widget.NetGraph(
                   border_width = 0,
                   graph_color = '#91b334',
                   fill_color = '#91b334',
                   frequency = 20,
                   #type = 'line',
                   #line_width = 0.5,
                ),

                # EXTRA WIDGETS
                # widget.CPUGraph(
                #    #border_color = '#2d333d',
                #    border_width = 0,
                #    graph_color = '#cf3521',
                #    fill_color = '#cf3521',
                #    frequency = 5,
                # ),
                
                # widget.Sep(
                #     linewidth = 1,
                #     padding = 20,
                #     foreground = win_sep,
                # ),

                widget.CPU(
                    font = 'ComicShannsMonoNerdFont',
                    foreground = '#4378b5',
                    format = '  CPU {load_percent}%', 
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 20,
                    foreground = win_sep,         
                ),

                widget.Memory(
                    font = 'ComicShannsMonoNerdFont',
                    foreground = '#a4ba34',
                    format = 'Memory {MemUsed:.0f}{mm}',
                ),
                widget.Sep(
                    linewidth = 1,
                    padding = 20,
                    foreground = win_sep,         
                ),

                widget.Clock(
                    format="  %Y-%m-%d %a %I:%M %p ",
                    font = 'ComicShannsMonoNerdFont',
                    fontsize = 13,
                    foreground = '#7e62a6',
                    center_aligned = True,
                ),
                widget.Systray(),
            ],
            22,
            background = '#101713',
            #margin = [0, 0, 0, 0],
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    border_focus='#9db548',
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "LG3D"

def autostart():
    subprocess.call(["/home/emon/.config/qtile/autostart.sh"])

autostart()
