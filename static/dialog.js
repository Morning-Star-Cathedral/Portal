;(function(){
  const modal = new bootstrap.Modal(document.getElementById('modal'), options)
  htmx.on('htmx:afterSwap', (e)=> {
    if (e.detail.target.id === "dialog")
      modal.show()
  })

})()
