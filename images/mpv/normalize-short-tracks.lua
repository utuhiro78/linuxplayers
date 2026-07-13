-- Author: UTUMI Hirosi (utuhiro78 at yahoo dot co dot jp)
-- License: GPL-2.0-or-later

local utils = require 'mp.utils'

-- Analyze tracks shorter than max_duration seconds
-- Non-dynamic normalization takes a lot of time for long duration tracks
local max_duration = 480
local onscreen_time = 3
local null_device = package.config:sub(1,1) == "\\" and "NUL" or "/dev/null"

local function get_duration(file)
    local res = mp.command_native({
        name = "subprocess",
        capture_stdout = true,
        args = {"ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", file}
    })

    -- Remove characters except numbers and dots
    local duration = res.stdout:gsub("[^%d%.]", "")
    return tonumber(duration)
end

local function get_max_volume(file)
    local res = mp.command_native({
        name = "subprocess",
        capture_stderr = true,
        args = {"ffmpeg", "-i", file, "-vn", "-filter:a", "volumedetect", "-f", "null", null_device}
    })

    local max_vol = string.match(res.stderr, "max_volume: ([%-%d%.]+) dB")
    return tonumber(max_vol)
end

-- "on_load" pauses playback until analysis
mp.add_hook("on_load", 50, function()
    local path = mp.get_property("path")

    if not path then
        print("Skip analysis: Empty path.")
        return
    elseif path:match("^%a+://") then
        print("Skip analysis: Network stream.")
        return
    elseif path:match("%.m3u$") then
        print("Skip analysis: M3U path. Check files in the list next.")
        return
    elseif path:find("/media/") then
        local msg = string.format("Skip analysis: /media/ files can be slow.")
        print(msg)
        mp.osd_message(msg, onscreen_time)
        return
    end

    local ext = path:match("%.([^%.]+)$")
    if ext and ext:lower() == "cue" then
        local msg = string.format("Skip analysis: Can't analyze CUE files.")
        print(msg)
        mp.osd_message(msg, onscreen_time)
        return
    end

    -- Get duration
    local duration = get_duration(path)
    if not duration then
        print("Skip analysis: Unrecognized format.")
        mp.command("playlist-next")
        return
    end

    if duration > max_duration then
        local msg = string.format("Skip analysis: Duration > " .. max_duration .. " seconds.")
        print(msg)
        mp.osd_message(msg, onscreen_time)
        return
    end

    -- Get max volume
    local filename = path:match("([^/\\]+)$") or path
    print("Analyzing max volume: " .. filename)

    local max_vol = get_max_volume(path)
    local volume_gain = 0 - max_vol

    -- Apply volume-gain
    mp.set_property("volume-gain", volume_gain)
    
    local msg = string.format("Max volume: %.1f dB | Gain: %.1f dB", max_vol, volume_gain)
    print(msg)
    mp.osd_message(msg, onscreen_time)
end)
