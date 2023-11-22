import React from "react";
import "./Login.css";
export const Login = () => {
  return (
    <div className="desktop">
      <div className="overlap-wrapper">
        <div className="overlap">
          <div className="frame">
            <div className="div">
              <h1>AfroPix</h1>
              <div className="overlap-group-wrapper">
                <div className="overlap-group">
                  <div className="frame-2">
                    <form action="/submit" method="post">
                      <label className="text-wrapper" for="email">
                        Email
                      </label>
                      <input
                        className="frame-3"
                        type="email"
                        id="email"
                        name="email"
                        required
                      />
                      <label className="text-wrapper-2" for="password">
                        Password
                      </label>

                      <input
                        className="frame-4"
                        type="password"
                        id="password"
                        name="password"
                        required
                      />
                      <div className="frame-7">
                        <input
                          className="text-wrapper-9"
                          type="submit"
                          value="Login"
                        ></input>
                      </div>
                    </form>

                    <div className="frame-7">
                      <div className="text-wrapper-9">LOG IN</div>
                    </div>

                    <div className="overlap-group-2">
                      <div className="frame-5">
                        <div className="text-wrapper-3">remember me</div>
                        <p className="not-a-member-sign-up">
                          Not a Member? Sign Up&nbsp;&nbsp;Here
                        </p>
                        <div className="text-wrapper-4">OR</div>
                        <div className="text-wrapper-5">forgot password ?</div>
                        <div className="rectangle" />
                        <img
                          className="vector"
                          alt="Vector"
                          src="vector-1.svg"
                        />
                        <img className="img" alt="Vector" src="vector-2.svg" />
                      </div>
                    </div>
                  </div>
                  <a
                    className="login-with-FB"
                    href="https://www.facebook.com/login.php/"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <div className="overlap-2">
                      <div className="log-in-with-facebook-wrapper">
                        <p className="log-in-with-facebook">
                          <span className="span">Continue with </span>
                          <span className="text-wrapper-8">Facebook</span>
                        </p>
                      </div>
                      <img
                        className="vector-2"
                        alt="Vector"
                        src="/vector.svg"
                      />
                    </div>
                  </a>

                  <a
                    className="login-with-google"
                    href="https://accounts.google.com/InteractiveLogin/identifier?elo=1&amp;ifkv=AVQVeyw7bFuoTPRBaszuPxQWTP7FSeyEFcI-VY-_2_zzgujULlhzGpHSwaWetysMOMp1pKUiBgj_&amp;theme=glif&amp;flowName=GlifWebSignIn&amp;flowEntry=ServiceLogin"
                    rel="noopener noreferrer"
                    target="_blank"
                  >
                    <div className="frame-8">
                      <div className="text-wrapper-10">
                        Continue with Google
                      </div>
                      <img
                        className="frame-9"
                        alt="Frame"
                        src="/google-icon-1@2x.png"
                      />
                    </div>
                  </a>
                </div>
              </div>
            </div>
          </div>
          <div className="frame-10">
            <div className="overlap-3">
              <div className="rectangle-wrapper">
                <div className="rectangle-2" />
              </div>
              <img
                className="carpenter"
                alt="Carpenter"
                src="/carpenter@2x.png"
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
