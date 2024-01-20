local M = {}

local autocmd = vim.api.nvim_create_autocmd
local augroup = vim.api.nvim_create_augroup

function M.setup()
    local group = augroup("shishifubing", { clear = true })

    -- highlight on yank
    autocmd({ "TextYankPost" }, {
        callback = function()
            vim.highlight.on_yank()
        end,
        group = augroup("YankHighlight", { clear = true }),
        pattern = "*",
    })
    -- remove trailing spaces
    autocmd({ "BufWritePre" }, {
        group = group,
        pattern = "*",
        command = "%s/\\s\\+$//e",
    })
end

return M
