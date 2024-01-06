# Dyslexia Helper

#### Step 1: Upload all of the files to VSCode
#### Step 2: Press Run --> Run without Debugging
#### Step 3: In the terminal, type python app.py and press Enter
#### Step 4: Click the link that looks like "http://192.168.2.182:5000" in the terminal


#### __Inspiration__: I knew that literacy rates in the United States have dropped below 80% last year, and that only 54% of adults can read at a 6th grade level. Also, I have received the advice "Visualize what you are reading" too often, and so I stumbled on the idea of generating images automatically for people in an attempt to boost reading comprehension.

#### **What it does**: Word Canvas is a website that uses state-of-the-art machine learning models to provide images for a text real-time as an aid.

#### **How I built it**: The website's user interface is coded in index.html and story.html, styled with app.css. The machine learning part in ml.py uses ChatGPT 3.5 and Dall-E 2 APIs to summarize text and generate images, seamlessly integrated into the website through app.py.

#### **Challenges I ran into**: The main error that I kept getting had to do with the prompts that I was entering into the APIs. It is a known problem that Dall-E 2, or image generation models in general, have a problem including text into their images as it often turn illegible. However, my pictures were often containing text, which is an issue that took a lot of troubleshooting to get around.

#### **Accomplishments that I'm proud of**: I am proud of the user interface because to me, it looks clean and very professional. Additionally, I am proud of the accuracy of the images in relation to the text.

#### **What I learned**: This is my first time using the ChatGPT and Dall-E 2 API, so I learned a lot about how it is implement and how to prompt these APIs to get exactly what I needed.

#### **What's next for Word Canvas**: In the future, I plan to make a database where people can log in and have an account for this website. They should be able to download their own text as a pdf, and the website should be able to read it and set up a page for it.



## You should now be able to access the website
