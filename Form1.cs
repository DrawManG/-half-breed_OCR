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

                // тут будет создание таблицы
                DataTable workTable = new DataTable("Customers");
                workTable.Columns.Add("№ п/п", typeof(String));
                workTable.Columns.Add("Номер", typeof(String));
                workTable.Columns.Add("Дата привоза", typeof(String));
                workTable.Columns.Add("Исполнитель", typeof(String));
                workTable.Columns.Add("Наименование выработки", typeof(String));
                workTable.Columns.Add("Глубина, м", typeof(String));
                workTable.Columns.Add("Состояние образца", typeof(String));
                workTable.Columns.Add("Описание", typeof(String));
                workTable.Columns.Add("Р, бар", typeof(String));
                workTable.Columns.Add("Р, кН", typeof(String));
                workTable.Columns.Add("S", typeof(String));
                dataGridView1.DataSource = new DataView(workTable);
                // тут будет подключение к питону

                // тут будет создание Парсинг изображений
                string s = label2.Text + @"\" + label3.Text + ".jpg";
                pictureBox1.ImageLocation = Path.Combine(s);
                string ppath = @"C:\temp\path.txt";
                // This text is added only once to the file.
                if (!File.Exists(ppath))
                {
                    // Create a file to write to.
                    using (StreamWriter sw = File.CreateText(ppath))
                    {
                        sw.WriteLine(label2.Text);
                    }

                }
            }
            }

        private void Button1_Click(object sender, EventArgs e)
        {
            // кнопка назад
            int numb = Convert.ToInt32(label3.Text);
            numb = numb - 1;
            if(numb <= 0)
            {
                MessageBox.Show("Ошибка. Вы вышли за лимит");
                numb = 1;
            }
            label3.Text = Convert.ToString(numb);
            string s = label2.Text + @"\" + label3.Text + ".jpg";
            pictureBox1.ImageLocation = Path.Combine(s);


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
            string s = label2.Text + @"\" + label3.Text + ".jpg";
            pictureBox1.ImageLocation = Path.Combine(s);
        }

        private void OCR_FORM_FormClosed(object sender, FormClosedEventArgs e)
        {
            File.Delete(@"C:\temp\path.txt");
        }
    }
}
