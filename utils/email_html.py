from jinja2 import Template
html_template = Template('''                     
<html>
  <body>
    <div id="mail-content-container" data-test="mail-content-container">
      <div style="display: flex !important; width: 100% !important">
        <div
          style="
            width: 100% !important;
            font-weight: 380;
            overflow-wrap: anywhere;
            -webkit-font-smoothing: antialiased;
          "
        >
          <div style="display: none">
            Please verify your email address to complete registration
          </div>
          <table
            bgcolor="#F2F2F2"
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="color: unset"
          >
            <tbody>
              <tr>
                <td>
                  <div
                    style="
                      max-width: 600px;
                      margin: 0 auto;
                      font-size: 16px;
                      line-height: 24px;
                    "
                  >
                    <table
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      width="100%"
                      style="color: unset"
                    >
                      <tbody>
                        <tr>
                          <td>
                            <table
                              border="0"
                              cellpadding="0"
                              cellspacing="0"
                              class="card-box first"
                              width="100%"
                              style="color: unset"
                            >
                              <tbody>
                                <tr>
                                  <td>
                                    <table
                                      border="0"
                                      cellpadding="0"
                                      cellspacing="0"
                                      class="card-box"
                                      width="100%"
                                      style="color: unset"
                                    >
                                      <tbody>
                                        <tr>
                                          <td
                                            style="
                                              background-color: white;
                                              padding-top: 30px;
                                              padding-bottom: 30px;
                                            "
                                            class="card"
                                          >
                                            <table
                                              border="0"
                                              cellpadding="0"
                                              cellspacing="0"
                                              width="100%"
                                              style="color: unset"
                                            >
                                              <tbody>
                                                <tr>
                                                  <td
                                                    align="left"
                                                    style="
                                                      padding-top: 0;
                                                      padding-bottom: 20px;
                                                      padding-left: 30px;
                                                    "
                                                  >
                                                    <!-- <a
                                                      href=""
                                                    > -->
                                                      <h1 style="color:#14a800">Trading Buddy</h3>
                                                    <!-- </a> -->
                                                  </td>
                                                </tr>
                                                <tr>
                                                  <td
                                                    class="card-row"
                                                    style="
                                                      font-family: Helvetica,
                                                        Arial, sans-serif;
                                                      font-size: 16px;
                                                      line-height: 24px;
                                                      word-break: break-word;
                                                      padding-left: 20px;
                                                      padding-right: 20px;
                                                      padding-top: 20px;
                                                      padding-bottom: 20px;
                                                      margin-left: px;
                                                      margin-right: px;
                                                    "
                                                  >
                                                    <h2
                                                      style="
                                                        margin-top: 0;
                                                        margin-bottom: 0;
                                                        font-family: Helvetica,
                                                          sans-serif;
                                                        font-weight: normal;
                                                        font-size: 24px;
                                                        line-height: 30px;
                                                        color: #001e00;
                                                      "
                                                    >
                                                      Verify your email address
                                                      to complete registration
                                                    </h2>
                                                  </td>
                                                </tr>
                                                <tr>
                                                  <td
                                                    class="card-row"
                                                    style="
                                                      font-family: Helvetica,
                                                        Arial, sans-serif;
                                                      font-size: 16px;
                                                      line-height: 24px;
                                                      word-break: break-word;
                                                      padding-left: 20px;
                                                      padding-right: 20px;
                                                      padding-top: 20px;
                                                      margin-left: px;
                                                      margin-right: px;
                                                    "
                                                  >
                                                    Hi {{firstName}}
                                                  </td>
                                                </tr>
                                                <tr>
                                                  <td
                                                    class="card-row"
                                                    style="
                                                      font-family: Helvetica,
                                                        Arial, sans-serif;
                                                      font-size: 16px;
                                                      line-height: 24px;
                                                      word-break: break-word;
                                                      padding-left: 20px;
                                                      padding-right: 20px;
                                                      padding-top: 20px;
                                                      margin-left: px;
                                                      margin-right: px;
                                                    "
                                                  >
                                                    Thanks for your interest in
                                                    joining Trading Buddy! To complete
                                                    your registration, we need
                                                    you to verify your email
                                                    address.
                                                  </td>
                                                </tr>
                                                <tr>
                                                  <td
                                                    class="card-row"
                                                    style="
                                                      font-family: Helvetica,
                                                        Arial, sans-serif;
                                                      font-size: 16px;
                                                      line-height: 24px;
                                                      word-break: break-word;
                                                      padding-left: 20px;
                                                      padding-right: 20px;
                                                      padding-top: 40px;
                                                      padding-bottom: 20px;
                                                      margin-left: px;
                                                      margin-right: px;
                                                    "
                                                  >
                                                    <table
                                                      style="
                                                        text-align: center;
                                                        color: unset;
                                                      "
                                                      width="100%"
                                                      border="0"
                                                      cellspacing="0"
                                                      cellpadding="0"
                                                    >
                                                      <tbody>
                                                        <tr>
                                                          <td>
                                                            <div
                                                              class="button-holder"
                                                              style="
                                                                text-align: center;
                                                                margin: 0 auto;
                                                              "
                                                            >
                                                              <a
                                                                style="
                                                                  background-color: #14a800;
                                                                  border: 2px
                                                                    solid
                                                                    #14a800;
                                                                  border-radius: 100px;
                                                                  min-width: 230px;
                                                                  color: #ffffff;
                                                                  white-space: nowrap;
                                                                  font-weight: normal;
                                                                  display: block;
                                                                  font-family: Helvetica,
                                                                    Arial,
                                                                    sans-serif;
                                                                  font-size: 16px;
                                                                  line-height: 40px;
                                                                  text-align: center;
                                                                  text-decoration: none;
                                                                  -webkit-text-size-adjust: none;
                                                                  mso-hide: all;
                                                                "
                                                                href="https://www.tradingbuddytools.com/verify/{{token}}"
                                                                >Verify Email</a
                                                              >
                                                            </div>
                                                          </td>
                                                        </tr>
                                                      </tbody>
                                                    </table>
                                                  </td>
                                                </tr>
                                                <tr>
                                                  <td
                                                    class="card-row"
                                                    style="
                                                      font-family: Helvetica,
                                                        Arial, sans-serif;
                                                      font-size: 16px;
                                                      line-height: 24px;
                                                      word-break: break-word;
                                                      padding-left: 20px;
                                                      padding-right: 20px;
                                                      padding-top: 20px;
                                                      margin-left: px;
                                                      margin-right: px;
                                                    "
                                                  >
                                                    Please note that not all
                                                    applications to join Trading
                                                    Buddy are accepted. We will
                                                    notify you of our decision
                                                    by email within 24 hours.
                                                  </td>
                                                </tr>
                                                <tr>
                                                  <td
                                                    class="card-row"
                                                    style="
                                                      font-family: Helvetica,
                                                        Arial, sans-serif;
                                                      font-size: 16px;
                                                      line-height: 24px;
                                                      word-break: break-word;
                                                      padding-left: 20px;
                                                      padding-right: 20px;
                                                      padding-top: 30px;
                                                      margin-left: px;
                                                      margin-right: px;
                                                    "
                                                  >
                                                    <div
                                                      style="padding-top: 10px"
                                                    >
                                                      Thanks for your time,<br />The
                                                      Trading Buddy Team
                                                    </div>
                                                  </td>
                                                </tr>
                                              </tbody>
                                            </table>
                                          </td>
                                        </tr>
                                      </tbody>
                                    </table>
                                  </td>
                                </tr>
                              </tbody>
                            </table>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <table
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      width="100%"
                      style="color: unset"
                    >
                      <tbody>
                        <tr>
                          <td
                            align="center"
                            width="100%"
                            style="
                              color: #65735b;
                              font-size: 12px;
                              line-height: 24px;
                              padding-bottom: 30px;
                              padding-top: 30px;
                            "
                          >
                            <a
                              href="https://www.tradingbuddytools.com/"
                              style="color: #65735b; text-decoration: underline"
                              >Privacy Policy</a
                            >
                            &nbsp; | &nbsp;
                            <a
                              href="https://www.tradingbuddytools.com/"
                              style="color: #65735b; text-decoration: underline"
                              >Contact Support</a
                            >
                            <div
                              style="
                                font-family: Helvetica, Arial, sans-serif;
                                word-break: normal;
                              "
                              class="address-link"
                            >
                              Montgomery Street, San Francisco, CA 78456
                            </div>
                            <div
                              style="
                                font-family: Helvetica, Arial, sans-serif;
                                word-break: normal;
                              "
                            >
                              © 2023 Trading Buddy Inc.
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </body>
</html>

''')