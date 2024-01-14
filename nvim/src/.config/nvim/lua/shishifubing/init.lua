local M = {}

function M.setup()
    vim.g.mapleader = " "
    vim.g.maplocalleader = " "
    require("shishifubing.lazy").setup()
    require("shishifubing.options").setup()
    require("shishifubing.autocmd").setup()
    require("shishifubing.filetypes").setup()
    require("shishifubing.keymaps").setup_no_deps()
end

return M
