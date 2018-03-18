import Template from './_template.js';
const centeredStyle = {position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)'};

export default () => <Template>
<form action="mailto:ttb@princeton.edu" method="post" encType="text/plain" style={centeredStyle}>
Name:<br/>
<input type="text" name="name"/><br/>
E-mail:<br/>
<input type="text" name="mail"/><br/>
Message:<br/>
<input type="text" placeholder="Suggestions?" name="comment" size="50"/><br/>
<input type="submit" value="Send"/>
</form>
</Template>
