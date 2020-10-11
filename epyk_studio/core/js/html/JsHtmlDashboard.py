

from epyk.core.js.html import JsHtml
from epyk.core.js.primitives import JsObjects
from epyk.core.js import JsUtils


class JsHtmlColumns(JsHtml.JsHtml):

  @property
  def val(self):
    """
    Description:
    ------------
    Return the standard value object with the fields (value, timestamp, offset).
    """
    return JsObjects.JsObjects.get(
      "{%s: {value: %s.querySelector('[data-select=true]').innerHTML, timestamp: Date.now(), offset: new Date().getTimezoneOffset()}}" % (self.htmlCode, self.varName))

  @property
  def content(self):
    """
    Description:
    ------------
    Return the values of the items in the list.
    """
    return JsObjects.JsArray.JsArray.get('''
      (function(){
         var values = []; %(component)s.querySelectorAll("li").forEach(function(dom){values.push(dom.innerText)});
         return values
      })()''' % {"component": self._src.dom.varName})

  @property
  def classList(self):
    """
    Description:
    ------------
    Return the class name of the list item.
    """
    return self._src.dom.getAttribute("class")

  def add(self, item, unique=True, draggable=True):
    """
    Description:
    ------------
    Add a new item to the list.

    Attributes:
    ----------
    :param item: String. The Item to be added to the list.
    :param unique: Boolean. optional. Only add the item if it is not already in the list.
    :param draggable: Boolean. Optional. Set the new entry as draggable
    """
    if hasattr(item, 'dom'):
      item = item.dom.content
    item = JsUtils.jsConvertData(item, None)
    unique = JsUtils.jsConvertData(unique, None)
    draggable = JsUtils.jsConvertData(draggable, None)
    return JsObjects.JsVoid('''
      var listItems = %(item)s; 
      if(!Array.isArray(listItems)){listItems = [listItems]};
      listItems.forEach(function(item){
        var li = document.createElement("li");
        if(%(unique)s){
          var hasItems = false;
          %(component)s.querySelectorAll("li").forEach(function(dom){
            if (dom.innerText == item){hasItems = true}})
          if(!hasItems){
            var text = document.createElement("div"); text.innerText = item;
            text.style.display = 'inline-block';
            text.style['margin-right'] = '10px';
            text.addEventListener("click", function(event){
              if (document.selection) {
                var range = document.body.createTextRange();
                range.moveToElementText(event.srcElement);
                range.select().createTextRange();
                document.execCommand("copy");
              } else if (window.getSelection) {
                var range = document.createRange();
                range.selectNode(event.srcElement);
                window.getSelection().addRange(range);
                document.execCommand("copy");
                alert("Text has been copied, now paste in the text-area")
              }
            });
            if (%(draggable)s){
              text.setAttribute('draggable', true);
              text.addEventListener('dragstart', function(event){event.dataTransfer.setData("text", event.target.innerHTML)} )
            }
            var div = document.createElement("div"); div.appendChild(text);
            var span = document.createElement("span"); span.innerHTML = '&#10006';  div.appendChild(span);
            span.addEventListener("click", function(){li.remove()});
            span.style.display = 'inline-block';
            
            li.appendChild(div); li.style.cursor = "pointer"; li.style['text-align'] = "left";
            %(component)s.appendChild(li)}
        }else{
          var text = document.createElement("div"); text.innerText = item;
          if (%(draggable)s){
            text.setAttribute('draggable', true);
            text.addEventListener('dragstart', function(event){event.dataTransfer.setData("text", event.target.innerHTML)} )
          }
          var div = document.createElement("div"); div.appendChild(text);
          li.appendChild(div); li.style.cursor = "pointer"; li.style['text-align'] = "left";
          %(component)s.appendChild(li)
        }
      })''' % {"item": item, "component": self._src.dom.varName, 'unique': unique, 'draggable': draggable})

  def clear(self):
    """
    Description:
    ------------
    Clear all the items in the list.
    """
    return JsObjects.JsVoid("%s.innerHTML = ''" % self._src.dom.varName)

  def loading(self, label="Processing data"):
    """
    Description:
    ------------

    :param label:
    """
    return JsObjects.JsVoid("%s.innerHTML = '<i style=\"margin-right:5px\" class=\"fas fa-spinner fa-spin\"></i>%s'" % (self._src.dom.varName, label))
