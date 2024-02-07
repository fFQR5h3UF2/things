local bg = "#333333"
local fg = "#ffffff"

local colors = {
    a = { bg = fg, fg = bg },
    b = { bg = bg, fg = fg },
    c = { bg = bg, fg = fg },
}
local theme = {
    normal = colors,
    insert = colors,
    visual = colors,
    replace = colors,
    command = colors,
    inactive = colors,
}

return {
    "nvim-lualine/lualine.nvim",
    opts = {
        options = {
            globalstatus = true,
            theme = theme,
            icons_enabled = false,
            component_separators = "|",
            section_separators = "",
        },
    },
}
