import Template from './_template.js';
import Link from 'next/link/';

const videoStyle = {position: 'absolute',
    right: 0,
    minWidth: "100%",
    zIndex: 2};
    
const footerStyle = {position: "fixed",
  bottom: 0,
  left: 0,
  right: 0,
  padding: '9px',
  backgroundColor: '#999',};

const linkStyle = {background: '#111',
  borderRadius: '3px',
  padding: '5px',
  color: 'white'};

const centeredStyle = {position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)'};

export default () => <Template>

<img style={centeredStyle} src="https://lh3.googleusercontent.com/_PmKhiJF_lVuZNj9kyM8TL-BXhKmYuwm2jgm6QjjwkhKMnnQLbuHVbjKr1LtXOPf6fYe7PjNbnXAbxsrD3FJO7Hu41p7rzFwmmkCN48HlDzon3OEeCA9NbkcPoOKLjYMlSmTAQpNlAS31QOYmw"/>
<video autoPlay muted loop style={videoStyle} src="/static/ant_path_2.mp4" type="video/mp4"/>

<footer style={footerStyle}>
<Link href="/contact"><a style={linkStyle}>Contact Us</a></Link>
</footer>
</Template>
