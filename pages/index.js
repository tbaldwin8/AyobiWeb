import Template from './_template.js';
import Link from 'next/link/';
import React from 'react';

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

//<!--<h3 style="line-height:1.5;"> Ayobi is your guide for the most difficult journey in life: fitness. Losing weight, gaining muscle, looking good, feeling great, or simply just staying fit, whatever your destination is, there is someone else who has already found a way to get there. Ayobi harnesses the power of the community to get you from any Point A to any Point B in fitness as quickly, effectively, and enjoyably as possible. </h3>-->
/*<!-- <p class="lead">
  <a class="btn btn-primary btn-lg" href="#" role="button">Sign Up Today</a>
  </p> -->*/
// <!-- Begin MailChimp Signup Form -->
// <!--<div class="indicates-required"><span class="asterisk">*</span> indicates required</div>--> 
//<!--<label for="mce-EMAIL" style="color: white;">Email Address <span class="asterisk">*</span>
  // </label>-->
/*
<!--<div class="mc-field-group">
  <label for="mce-FNAME">First Name </label>
<input type="text" value="" name="FNAME" class="" id="mce-FNAME" placeholder="Todd">
</div>
<div class="mc-field-group">
<label for="mce-LNAME">Last Name </label>
<input type="text" value="" name="LNAME" class="" id="mce-LNAME" placeholder="Baldwin">
</div>
<div id="mce-responses" class="clear">
<div class="response" id="mce-error-response" style="display:none"></div>
<div class="response" id="mce-success-response" style="display:none"></div>
</div>  -->*/

/* <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups--> */
// <!--End mc_embed_signup-->
class Index extends React.Component {
  render() {
    return (
      <Template><div>
        <nav className="navbar navbar-expand-lg" style={{backgroundColor: 'transparent'}}/>
          <a className="navbar-brand" href="#" id="header" style={{backgroundColor: 'transparent'}}>
            {/*<img src="/assets/logo1.png">*/}
            <h1 style={{color: '#fff', fontSize: 48, marginLeft:'1vw'}}>AYOBI</h1>
          </a>
          <div className="container">
            <div className="container" id="words">
              <h1 style={{color: 'white'}}> Fitness is a Journey. Let's work together to find the best path to our fitness.</h1>
              {/*<h3 style="line-height:1.5;"> Ayobi is your guide for the most difficult journey in life: fitness. Losing weight, gaining muscle, looking good, feeling great, or simply just staying fit, whatever your destination is, there is someone else who has already found a way to get there. Ayobi harnesses the power of the community to get you from any Point A to any Point B in fitness as quickly, effectively, and enjoyably as possible. </h3>*/}
            </div>
            {/* <p class="lead">

<a class="btn btn-primary btn-lg" href="#" role="button">Sign Up Today</a>
</p> */}
            <div className="container" id="box">
              {/* Begin MailChimp Signup Form */}
              <link href="//cdn-images.mailchimp.com/embedcode/classic-10_7.css" rel="stylesheet" type="text/css" />
              <style type="text/css" dangerouslySetInnerHTML={{__html: "\n#mc_embed_signup{background: transparent; height: 500px; clear:left; font:14px Helvetica,Arial,sans-serif; }\n/* Add your own MailChimp form style overrides in your site stylesheet or in this style block.\n   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. mc-embedded-subscribe-form*/\n" }} />
              <div id="mc_embed_signup">
                <form action="https://herokuapp.us18.list-manage.com/subscribe/post?u=386df2f9defd59a915d318fba&id=7cc275a23c" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" className="validate" target="_blank" noValidate>
                  <div id="mc_embed_signup_scroll">
                    <h1 style={{fontSize: 18, letterSpacing: 10, color: '#333'}}>Subscribe to our mailing list</h1>
                    {/*<div class="indicates-required"><span class="asterisk">*</span> indicates required</div>*/} 
                    <div className="mc-field-group">
                      {/*<label for="mce-EMAIL" style="color: white;">Email Address <span class="asterisk">*</span>
</label>*/}
                      <input style={{backgroundColor: 'transparent', color: 'white', border: 'none', outline: 0, borderBottom: '1px white'}} type="email" name="EMAIL" className="required email" id="mce-EMAIL" placeholder="you@example.com" />
                    </div>
                    {/*<div class="mc-field-group">
<label for="mce-FNAME">First Name </label>
<input type="text" value="" name="FNAME" class="" id="mce-FNAME" placeholder="Todd">
</div>
<div class="mc-field-group">
<label for="mce-LNAME">Last Name </label>
<input type="text" value="" name="LNAME" class="" id="mce-LNAME" placeholder="Baldwin">
</div>
<div id="mce-responses" class="clear">
<div class="response" id="mce-error-response" style="display:none"></div>
<div class="response" id="mce-success-response" style="display:none"></div>
</div>  */}  {/* real people should not fill this in and expect good things - do not remove this or risk form bot signups*/}
                    <div style={{position: 'absolute', left: '-5000px'}} aria-hidden="true"><input type="text" name="b_386df2f9defd59a915d318fba_7cc275a23c" tabIndex={-1} defaultValue /></div>
                    <div className="clear"><input type="submit" defaultValue="Subscribe" name="subscribe" id="nbutton" className="btn btn-md btn-primary" style={{outline: 0, border: 'none'}} /></div>
                  </div>
                </form>
              </div>
              {/*End mc_embed_signup*/}
            </div>
          </div>
        </div>
      </Template>
    )
  }
};

export default Index;
/*export default () => <Template>*/

// <img style={centeredStyle} src="https://lh3.googleusercontent.com/_PmKhiJF_lVuZNj9kyM8TL-BXhKmYuwm2jgm6QjjwkhKMnnQLbuHVbjKr1LtXOPf6fYe7PjNbnXAbxsrD3FJO7Hu41p7rzFwmmkCN48HlDzon3OEeCA9NbkcPoOKLjYMlSmTAQpNlAS31QOYmw"/>
// <video autoplay muted loop id="myVideo" src="/static/ant_path_2.mp4" type="video/mp4"/>
// <footer style={footerStyle}>
// <Link href="/contact"><a style={linkStyle}>Contact Us</a></Link>
// </footer>
// </Template>

