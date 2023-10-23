/** Set up event listeners for the git history modal */
function setupGitHistory() {
  const checkbox = document.getElementById('history-checkbox')
  const background = document.getElementById('history-modal-background')
  const foreground = document.getElementById('history-modal-foreground')

  // Click on the background to close the modal
  background.onclick = () => {
    checkbox.checked = ''
  }

  // Prevent clicks on the table from closing the modal
  foreground.onclick = (event) => {
    event.stopPropagation()
  }

  // Listen for escape key to close modal
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && checkbox.checked) {
      checkbox.checked = ''
    }
  })
}

window.addEventListener('DOMContentLoaded', () => {
  setupGitHistory()
})
