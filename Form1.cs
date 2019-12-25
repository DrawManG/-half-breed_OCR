using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Half_Breed
{
    public partial class OCR_FORM : Form
    {
       
        public OCR_FORM()
        {
            InitializeComponent();
        }
       
        private void Button4_Click(object sender, EventArgs e)
        {
            using (var fbd = new FolderBrowserDialog())
            {
                //открыть окно для выбора папки
                DialogResult result = fbd.ShowDialog();
                //обработка результата
                if (result == DialogResult.OK && !string.IsNullOrWhiteSpace(fbd.SelectedPath))
                {
                    string[] files = Directory.GetFiles(fbd.SelectedPath);
                    label2.Text = fbd.SelectedPath;
                    label1.Text = Convert.ToString(files.Length);
                    System.Windows.Forms.MessageBox.Show("Files found: " + files.Length.ToString(), "Message");
                }
                // тут будет подключение к питону
            }
        }

        private void Button1_Click(object sender, EventArgs e)
        {
            // кнопка назад
            int numb = Convert.ToInt32(label3.Text);
            numb = numb - 1;
            if(numb < 0)
            {
                MessageBox.Show("Ошибка. Вы вышли за лимит");
                numb = 0;
            }
            label3.Text = Convert.ToString(numb);
            
        }

        private void Button2_Click(object sender, EventArgs e)
        {
            //кнопка вперёд
            int numb = Convert.ToInt32(label3.Text);
            numb = numb + 1;
            if (numb > Convert.ToInt32(label1.Text))
            {
                MessageBox.Show("Ошибка. Вы вышли за лимит");
                numb = Convert.ToInt32(label1.Text);
            }
            label3.Text = Convert.ToString(numb);
        }
    }
}
